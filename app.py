from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/index")
def index():

    return render_template("index.html", start=False)


@app.route("/levels", methods = ["GET", "POST"])
def levels():
    
    return render_template("index.html", start =True)


if __name__ == "__main__":
    app.run()