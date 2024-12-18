from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list to store tasks
tasks = []

# Home route
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks, enumerate=enumerate)

# Add a new task
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append({"task": task, "completed": False})
    return redirect(url_for("home"))

# Mark a task as completed
@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
    return redirect(url_for("home"))

# Delete a task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
