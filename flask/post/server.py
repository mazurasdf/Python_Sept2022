from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def form_page():
    return render_template("form.html")

@app.route("/sundaes/post", methods=["post"])
def sundae_submit():
    #do stuff with form info
    print(request.form["name"])
    print(request.form["flavor"])
    print(request.form["numScoops"])
    print(request.form["sauce"])
    print(request.form["topping1"])
    print(request.form["topping2"])

    if "whipped" in request.form:
        whipped = True
    else:
        whipped = False

    print(whipped)
    return redirect("/success")

@app.route("/success")
def success():
    return "you did it!"

if __name__ == "__main__":
    app.run(debug=True)