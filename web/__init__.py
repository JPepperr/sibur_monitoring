from flask import Flask, render_template, request, redirect
from database.models import Problems
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


@app.route('/show', methods=['GET'])
async def show():
    status = request.args.get('status', 'START')

    if status == 'START':
        problems = await Problems.filter(status='START').values()
    elif status == 'IN_PROGRESS':
        problems = await Problems.filter(status='IN_PROGRESS').values()
    elif status == 'END':
        problems = await Problems.filter(status='END').values()

    data = []
    for v in problems:
        data.append([v['description'], v['message'], v['time'], v['id']])

    data.sort(key=lambda x: x[2], reverse=True)

    return render_template('show.html', data=data, status=status)



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


def setup():
    app.run(host='127.0.0.1', port=8080, debug=True)
