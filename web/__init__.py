from flask import Flask, render_template, request, redirect
from database.models import Problems, Person
import datetime

app = Flask(__name__)


@app.route('/')
async def home():
    return render_template('home.html')


@app.route('/form')
async def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
async def submit():
    priority = request.form.get('priority')
    description = request.form.get('description')
    message = request.form.get('message')

    await Problems.create(priority=priority, description=description, message=message, status="START",
                          time=datetime.datetime.now())

    return render_template('success.html')


@app.route('/show')
async def show():
    tab = request.args.get('tab', 'start')  # Получаем вкладку, по умолчанию 'start'

    start_data = []
    in_progress_data = []
    end_data = []

    if tab == 'start':
        problems = await Problems.filter(status='START').values()
        for v in problems:
            start_data.append([v['description'], v['message'], v['time'], v['id'], 1])

        start_data.sort(key=lambda x: x[2], reverse=True)

    elif tab == 'in_progress':
        problems = await Problems.filter(status='IN_PROGRESS').all()
        for v in problems:
            in_progress_data.append([v.description, v.message, v.time, v.id, "<no>" if not v.responsible else (await v.responsible.first()).full_name])

        in_progress_data.sort(key=lambda x: x[2], reverse=True)

    elif tab == 'end':
        problems = await Problems.filter(status='END').all()
        
        for v in problems:
            end_data.append([v.description, v.message, v.time, v.id, "<no>" if not v.responsible else (await v.responsible.first()).full_name])

        end_data.sort(key=lambda x: x[2], reverse=True)

    return render_template('show.html',
                           start_data=start_data,
                           in_progress_data=in_progress_data,
                           end_data=end_data,
                           tab=tab)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
async def edit(id):
    problem = await Problems.get(id=id)
    if request.method == 'POST':
        problem.priority = request.form.get('priority')
        problem.description = request.form.get('description')
        problem.message = request.form.get('message')
        await problem.save()

        return redirect('/show')

    return render_template('edit.html', problem=problem)


@app.route('/take/<int:problem_id>', methods=['POST'])
async def take_problem(problem_id):
    problem = await Problems.get(id=problem_id)
    if problem:
        problem.status = 'IN_PROGRESS'
        await problem.save()
    return redirect('/show?tab=start')  # Возвращаемся на вкладку "Ждут действий"


@app.route('/solve/<int:problem_id>', methods=['POST'])
async def solve_problem(problem_id):
    problem = await Problems.get(id=problem_id)
    if problem:
        problem.status = 'END'  # Меняем статус задачи на "Решено"
        await problem.save()
    return redirect('/show?tab=in_progress')  # Возвращаемся на вкладку "В процессе"


def setup():
    app.run(host='127.0.0.1', port=5000, debug=True)
