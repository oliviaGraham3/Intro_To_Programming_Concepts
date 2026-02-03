money = 20
movie_cost = 14

if money >= movie_cost:
    print("YAYYY MOVIE TIME\n")

grade = 65

if (grade >= 90):
    print("You got an A")
elif(grade >= 80): #LOOK AT HER GO. LOOK. ELIF. WOW. NEW
    print("You got an B")
elif (grade >= 70):
    print("You got an C")
elif (grade >= 60):
    print("You got an D")
else:
    print("You got an F")


lang = "Python"

match lang: #wow match NEW. LOOK. Pretty much just == constantly
    case "Java":
        print("You are a Java programmer")
    case "Python":
        print("You are a Python programmer")
    #etc etc