from flask import Flask, render_template
from model import get_questions

app = Flask(__name__)
question_num = 4
level = 1
curr_answer = ""
earnings = 0
coffee_stocks = 0
correct_answer = False

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



@app.route("/financialvocab_game", methods = ["GET", "POST"])
def financialvocab_game():
    global level
    global question_num
    level = 1
    question_num = 4
    return game()



@app.route("/marketmaking", methods = ["GET", "POST"])
def marketmaking():
    return render_template("marketmaking.html")



@app.route("/marketmaking_game", methods = ["GET", "POST"])
def marketmaking_game():
    global level
    global question_num
    level = 2 
    question_num = 4
    return game()



@app.route("/game", methods = ["GET", "POST"])
def game():
    global question_num
    global level
    global curr_answer
    global earnings
    global coffee_stocks

    questions = get_questions()
    props = questions[level][question_num]
    curr_answer = props["answer"]

    return render_template("game.html", props=props, earnings=earnings, coffee_stocks=coffee_stocks)



@app.route("/check_a", methods = ["GET", "POST"])
def check_a():
    global curr_answer
    if curr_answer == "a":
        return correct()
    else:
        return incorrect()
    


@app.route("/check_b", methods = ["GET", "POST"])
def check_b():
    global curr_answer
    if curr_answer == "b":
        return correct()
    else:
        return incorrect()
    


@app.route("/check_c", methods = ["GET", "POST"])
def check_c():
    global curr_answer
    if curr_answer == "c":
        return correct()
    else:
        return incorrect()
    


@app.route("/check_d", methods = ["GET", "POST"])
def check_d():
    global curr_answer
    if curr_answer == "d":
        return correct()
    else:
        return incorrect()
    

    
@app.route("/correct", methods = ["GET", "POST"])
def correct():
    global earnings 
    global coffee_stocks
    global correct_answer

    
    props = {
        "earnings" : earnings,
        "coffee_stocks" : coffee_stocks,
    }
    
    return render_template("correct.html", props=props)



@app.route("/incorrect", methods = ["GET", "POST"])
def incorrect():

    global earnings 
    global coffee_stocks
    global correct_answer

    
    props = {
        "earnings" : earnings,
        "coffee_stocks" : coffee_stocks,
    }
    
    return render_template("incorrect.html", props=props)



@app.route("/next", methods = ["GET", "POST"])
def next():
    global question_num
    global level
    global correct_answer

    question_num -= 1
    correct_answer == False
    if question_num == 0:
        level += 1
        question_num = 4
        return level_over()
        
    return game()



@app.route("/level_over", methods = ["GET", "POST"])
def level_over():

    global earnings 
    global coffee_stocks

    props = {
        "earnings" : earnings,
        "coffee_stocks" : coffee_stocks,
    }

    return render_template("level_over.html", props=props)

@app.route("/stock", methods=["GET", "POST"])
def stock():

    global earnings 
    global coffee_stocks
    if correct_answer == False:
        earnings += 20
        coffee_stocks += 18
        correct_answer == True

    props = {
        "earnings" : earnings,
        "coffee_stocks" : coffee_stocks,
    }

    return render_template("stock.html", props=props)

@app.route("/order", methods = ["GET", "POST"])
def order():

    global earnings 
    global coffee_stocks

    props = {
        "earnings" : earnings,
        "coffee_stocks" : coffee_stocks,
    }

    return render_template("order.html", props=props)




if __name__ == "__main__":
    app.run(debug=True)