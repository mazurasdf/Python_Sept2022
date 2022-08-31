from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print("you're accessing the index route!")
    return "hey it's me, the main page!"

@app.route("/second")
def second():
    print("you're accessing the second route!")
    return "alright now this is the second page"

@app.route("/repeat/<phrase>")
def repeat_phrase(phrase):
    return f"your phrase is: {phrase}"

@app.route("/repeat/<phrase>/<int:times>")
def repeat_times(phrase,times):
    repeated = phrase * times
    return repeated

@app.route("/main")
def main():
    print("returning html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)