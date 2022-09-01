from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "it's a secret to everybody!"

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/submit_answer", methods=["post"])
def submit_answer():
    # print(request.form["answer"])
    session["answer"] = request.form["answer"]
    session["incorrect"] = ""

    progress = ""
    for letter in request.form["answer"]:
        if letter == " ":
            progress += " "
        else:
            progress += "_"
    session["progress"] = progress
    return redirect("/game")

@app.route("/game")
def game():
    if "answer" not in session:
        return redirect("/")

    print("session variable is:")
    print(session["answer"])
    return render_template("game.html")

@app.route("/reset")
def reset():
    # del session["answer"]
    session.clear()
    return redirect("/")

@app.route("/submit_guess", methods=["post"])
def submit_guess():
    answer = session["answer"].upper()
    guess = request.form["guess"].upper()
    progress = session["progress"].upper()

    if(guess in answer):
        new_progress = ""

        for i in range(len(answer)):
            if answer[i] == guess:
                new_progress += answer[i]
            else:
                new_progress += progress[i]
        session["progress"] = new_progress
    else:
        session["incorrect"] += guess

    return redirect("/game")

if __name__ == "__main__":
    app.run(debug=True)