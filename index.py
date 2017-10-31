import random

'''
Write a function that generates ten scores between 60 and 100. 
Each time a score is generated, your function should display what the grade is for a particular score.
'''

def score_grades():
    print "Scores and Grades"
    for i in range (0,10):
        numR = random.randint(60, 101)
        if numR >89:
            print "Score: {}; Your grade is A".format(numR)
        elif numR >79:
            print "Score: {}; Your grade is B".format(numR)
        elif numR >69:
            print "Score: {}; Your grade is c".format(numR)
        elif numR>59:
            print "Score: {}; Your grade is D".format(numR)

score_grades()
