from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def front_page():
    # contact database
    results = [
        {"user":"Mike","take":"Lord of the Rings sucks","score":3},
        {"user":"Danil","take":"Star Wars sequels are not good","score":200},
        {"user":"Some people","take":"crocs are sorta not that cool i think maybe","score":5},
        {"user":"Anthony","take":"Marvel is overrated","score":6},
        {"user":"Aman","take":"chinese food? meh not where it's at","score":-40},
    ]
    return render_template("front_page.html", results=results)

@app.route("/<phrase>")
def main(phrase):
    return render_template("main.html", phrase=phrase)

@app.route("/repeat/<phrase>/<int:times>")
def repeat(phrase, times):
    return render_template("repeat.html",phrase=phrase,times=times)

if __name__ == "__main__":
    app.run(debug=True)