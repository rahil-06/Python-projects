questions=("How many elements in periodic table?",
           "Which bird gives the largest egg?",
           "Which planet in the solar system is the hottes?")

options=(("A.116","B.117","C.119","D.119"),
         ("A.hen","B.eagle","C.crow","D.ostrich"),
         ("A.Mercury","B.venus","C.earth","D.mars"))
answers=("A","D","A")
question_num=0
scores=0
guesses=[]

for question in questions:
    print("-------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    guess=input("Enter your answer (A,B,C,D):")
    guesses.append(guess)

    if(guess==answers[question_num]):
        scores+=1
        print("CORRECT ANSWER")

    else:
        print("WRONG ANSWER")
    question_num += 1

print("----------")
print("RESULTS")
print("-----------")

print("Answers:",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses:",end="")
for guess in guesses:
    print(guess,end=" ")
print()

print("score is",scores)





