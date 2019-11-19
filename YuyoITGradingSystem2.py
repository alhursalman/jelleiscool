def grading(num): #Grades the grades
    if num >=99:
        return "U. No way you could have gotten that without cheating. (A****)"
    elif num >=94:
        return "S-Class Hero ranking. All might would be proud."
    elif num >= 87:
        return "A**. Either a prodigy or a cheater."
    elif num >= 79:
        return "A*. Hard work pays off!"
    elif num >= 70:
        return "A. First class grade."
    elif num >= 58:
        return "B. You payed enough attention in class. Well done!"
    elif num >= 42:
        return "C. You have passed and can still apply to the same jobs as everyone else smarter than you!"
    elif num >= 28:
        return "D."
    elif num >= 17:
        return "E."
    elif num >= 11:
        return "F. At least you can still put it on your CV."
    else:
        return "U, which is a fail. How on Earth did you manage to do that? It's only 11% to pass!"

def gradecalc(test1, test2, test3, maxgrade1, maxgrade2, maxgrade3):
    valid = True
    while valid:
        try:
            Home_Grade = float(input(test1))
            Assess_Grade = float(input(test2))
            Exam_Grade = float(input(test3))
            if Home_Grade > maxgrade1 or Assess_Grade > maxgrade2 or Exam_Grade > maxgrade3:
                print("One (or more) of your grades is higher than the maximum mark")
            elif Home_Grade < 0 or Assess_Grade < 0 or Exam_Grade < 0:
                print("You can't have negative marks")
            else:
                valid = False
        except ValueError:
            print("That is not a (valid) number.")
    #return [Home_Grade, Assess_Grade, Exam_Grade]
    return {
        "home": Home_Grade,
        "assess": Assess_Grade,
        "exam": Exam_Grade
    }

def thecode():
    print ("Virtual report card.")
    first = input("First Name:")
    last = input("Last Name:")
    grades = gradecalc("Homework grade out of 25: ","Assessment grade out of 50: ","Final exam grade out of 100: ",25,50,100)
    score = round((grades["home"]*4*0.25 + grades["assess"]*2*0.35 + grades["exam"]*0.45), 2)
    grade = grading(score)
    print(first, last, "got a score of: " + str(score) + ", This is a grade of: " + grade)


thecode()
