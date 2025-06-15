# app.py
from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks = load_tasks()
        tasks.append({"name": task})
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

# templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Minimal Task Manager</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h1>Mes Tâches</h1>
        <form action="/add" method="post">
            <input type="text" name="task" required>
            <button type="submit">Ajouter</button>
        </form>
        <ul>
            {% for task in tasks %}
                <li>{{ task.name }} <a href="/delete/{{ loop.index0 }}">❌</a></li>
            {% endfor %}
        </ul>
    </div>
    <script src="/static/script.js"></script>
</body>
</html>

# static/style.css
body {
    background: #121212;
    color: white;
    font-family: sans-serif;
    display: flex;
    justify-content: center;
}
.container {
    margin-top: 50px;
    width: 400px;
}
input, button {
    padding: 10px;
    border: none;
    margin-right: 5px;
}
button {
    background: #1db954;
    color: white;
    cursor: pointer;
}

# static/script.js
document.addEventListener("DOMContentLoaded", () => {
    console.log("Task Manager Loaded");
});

# tasks.json
[]

# run_server.bat
@echo off
cd /d %~dp0
python -m venv venv
call venv\Scripts\activate
pip install flask
echo Running server...
python app.py
pause

# requirements.txt
flask

# .gitignore
venv/
__pycache__/
tasks.json

# README.md
# 📝 Minimal Task Manager

Un gestionnaire de tâches minimaliste avec une interface web, développé avec Flask.

## Fonctionnalités
- Ajout et suppression de tâches
- Interface web simple et propre
- Sauvegarde automatique dans `tasks.json`

## Installation
1. Clone ou télécharge le projet.
2. Lance `run_server.bat`.
3. Va sur [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Auteur
**louisspjl** – fait avec ❤️ et Flask.
