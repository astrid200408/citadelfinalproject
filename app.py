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
    global curr_answer

    questions = get_questions()
    props = questions[level][question_num]
    curr_answer = props["answer"]
    
    return render_template("game.html", props=props)

@app.route("/check_a", methods = ["GET", "POST"])
def check_a():
    global curr_answer
    if curr_answer == "a":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")

@app.route("/check_b", methods = ["GET", "POST"])
def check_b():
    global curr_answer
    if curr_answer == "b":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")

@app.route("/check_c", methods = ["GET", "POST"])
def check_c():
    global curr_answer
    if curr_answer == "c":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")

@app.route("/check_d", methods = ["GET", "POST"])
def check_d():
    global curr_answer
    if curr_answer == "d":
        return render_template("correct.html")
    else:
        return render_template("incorrect.html")
    
@app.route("/correct", methods = ["GET", "POST"])
def correct():
    return render_template("correct.html")

@app.route("/incorrect", methods = ["GET", "POST"])
def incorrect():
    return render_template("incorrect.html")

@app.route("/next", methods = ["GET", "POST"])
def next():
    global question_num
    global level

    question_num -= 1
    if question_num == 0:
        level += 1
    return game()




if __name__ == "__main__":
    app.run(debug=True)