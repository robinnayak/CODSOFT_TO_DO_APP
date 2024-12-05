from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ["Example Task..."]
colors_combinations = {
    "text_color": "white",
    "bg_color": "linear-gradient(90deg,rgba(2, 0, 36, 1) 0%,rgba(14, 230, 54, 1) 0%,rgba(25, 30, 31, 1) 100%);",
    "btn_bg_color": "black",
}


@app.route("/")
def home_page():
    return render_template("index.html", tasks=tasks, colors=colors_combinations)


@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect("/")
    return render_template("add_task.html", colors=colors_combinations)


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
