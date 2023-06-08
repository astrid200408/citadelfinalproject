from flask import Flask, render_template
import requests
from model import get_questions


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/index")
def index():
    return render_template("index.html", start=False)


@app.route("/levels", methods = ["GET", "POST"])
def levels():
    return render_template("index.html", start =True)

@app.route("/financialvocab", methods = ["GET", "POST"])
def financialvocab():
    return render_template("financialvocab.html")

@app.route("/game", methods = ["GET", "POST"])
def game():
    props= get_questions()
    return render_template("game.html", props=props)



if __name__ == "__main__":
    app.run()