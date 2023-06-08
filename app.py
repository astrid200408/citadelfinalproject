from flask import Flask, render_template
import requests
from model import get_questions
import json



app = Flask(__name__)
question_num = 4
level = 1
curr_answer = ""

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

@app.route("/marketmaking", methods = ["GET", "POST"])
def marketmaking():
    return render_template("marketmaking.html")

@app.route("/game", methods = ["GET", "POST"])
def game():
    global question_num
    global level
    questions = get_questions()
    props = questions[level][question_num]
    curr_answer = props["answer"]
    print(curr_answer)
    question_num -= 1
    return render_template("game.html", props=props)

@app.route("/check_a", methods = ["GET", "POST"])
def check_a():
    if curr_answer == "a":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")

@app.route("/check_b", methods = ["GET", "POST"])
def check_b():
    if curr_answer == "b":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")

@app.route("/check_c", methods = ["GET", "POST"])
def check_c():
    if curr_answer == "c":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")

@app.route("/check_d", methods = ["GET", "POST"])
def check_d():
    if curr_answer == "d":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")




if __name__ == "__main__":
    app.run()