import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

tasks = load_tasks()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_title = request.form.get('task')
        if task_title:
            tasks.append({'title': task_title, 'done': False})
            save_tasks(tasks)
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
