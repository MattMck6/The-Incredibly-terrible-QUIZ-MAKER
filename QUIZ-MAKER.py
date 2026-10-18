
def board():
    print ("  |The Quiz|")
    print("\n  1.Create Quiz ")
    print("\n  2.Use Quiz ")
    print("\n  3.Quit ")
#try:
quiz_question=[]
def quiz(): 
    run=True
    while run==True:
        board()
        user=input("What would you like to do?")
        if "1" == user or "create" in user.lower():
            print ("Hi user put as many questions and answers as you want then put a # when your done")
            name=input("whats the quiz name?")
            while run==True:
                questions=input("whats the question?")
                answers=input("whats the answer?")
                if answers=="#" or questions=="#":
                    print("You have left the quiz maker")
                    break
                new_quiz={
                    "name":name,
                      "questions":questions,
                      "answers":answers
                      }
                quiz_question.append(new_quiz)
        elif "2" == user or "use" in user.lower():
            found=False
            score=0
            quiznames=set()
            if quiz_question=="":
                print ("error,No quizes available")
            for i in quiz_question:#
                quiznames.add(i["name"])
            print (quiznames)
            finder=input("Whats the quiz you want to use? ")
            for i in quiz_question:
                if i["name"].lower().strip()==finder.lower().strip():
                    found=True
                    answer=input(i["questions"]+" ")
                    if answer.lower().strip()==i["answers"].lower().strip():
                        score+=1
                        print ("Correct")
                    else:
                        print ("incorrect")
            if not found:
                print ("quiz not found")
            else:
                print ("Your score is",score)
        elif "3" == user or "quit" in user.lower():
            print ("You have quit")
            break
        else:
            print ("Error")
#except ValueError:
    #print ("Something went wrong")
        
quiz()