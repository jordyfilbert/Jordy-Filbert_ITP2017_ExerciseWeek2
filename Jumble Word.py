import re
import random
def question():
    answer = input("What will the first word be?")
    if answer == result:
        correct()
    else:
        wrong()

def correct():
    print ("You are correct")
def wrong():
    print ("Incorrect please retry")
    question()


print ("Welcome to jumble word game")
mystr = input("Please enter a sentence to be Jumbled")
wordList = re.sub("[^\w]", " ",  mystr).split()
random.shuffle(wordList)
result = wordList[0]
# print (wordList[0])
question()