from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_index = int(request.form['task_index'])
    del tasks[task_index]
    return redirect(url_for('index'))

@app.route('/complete_task', methods=['POST'])
def complete_task():
    task_index = int(request.form['task_index'])
    tasks[task_index] = f'<del>{tasks[task_index]}</del>'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
