from flask import Flask, render_template, request
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


@app.route('/show')
async def show():
    problems = await Problems.all().values()
    data = []
    for v in problems:
        data.append([v['description'], v['message'], v['time']])
        print(v['time'])

    data.sort(key=lambda x: x[2], reverse=True)

    return render_template('show.html', data=data)


def setup():
    app.run(host='127.0.0.1', port=8080, debug=True)
