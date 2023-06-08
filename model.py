import os

def get_questions():

    questions = []
    f = open('questions.txt','r')

    for x in f:
        questions.append(x)

    f.close()

