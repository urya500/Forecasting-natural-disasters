from flask import Flask, render_template, request, Response, redirect
from datamanger import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        country = request.form.get("countryInput")
        year = request.form.get("yearSelect")
        if country and year:
            plot = statics(country, int(year))
        return redirect("/")


    return render_template("index.html")

if __name__ == "__main__":
    app.run()
