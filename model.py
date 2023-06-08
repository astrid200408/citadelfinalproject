import os
import json

def get_questions():

    questions = {}
    f = open('questions.txt', 'r')

    quest_count = 5;
    level_count = 1;

    for x in f:
        
        my_dict = json.loads(x)
        print(my_dict["question"])

        if quest_count ==5 :
            # add first dict to level
            new_list = []
            new_list.append(my_dict)
            quest_count-=1

        elif quest_count == 1:

            # adds last dict to level and 
            new_list.append(my_dict)
            questions[level_count] = new_list

            # go to next level 
            quest_count == 5
            level_count+=1

        else:

            new_list.append(my_dict)
            quest_count -= 1
    
    f.close()

    return questions

print(get_questions())
    

