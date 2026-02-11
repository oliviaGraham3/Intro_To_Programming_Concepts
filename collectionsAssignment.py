studentName = input("Name: ")
gradeList = []
letterGrade = ""

grade1 = int(input("Enter your grade: "))
gradeList.append(grade1)

grade2 = int(input("Enter your grade: "))
gradeList.append(grade2)

grade3 = int(input("Enter your grade: "))
gradeList.append(grade3)

grade4 = int(input("Enter your grade: "))
gradeList.append(grade4)

grade5 = int(input("Enter your grade: "))
gradeList.append(grade5)

avg = (gradeList[0] + gradeList[1] + gradeList[2] + gradeList[3] + gradeList[4])/ len(gradeList)

if avg < 0 or avg > 100:
    letterGrade = "OOR"
elif avg >= 90:
    letterGrade = "A"
elif avg >= 80:
    letterGrade = "B"
elif avg >= 70:
    letterGrade = "C"
elif avg >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

if letterGrade != "OOR":
    print(studentName)
    print("Average: " , avg)
    print("Letter Grade: " , letterGrade)
elif letterGrade == "OOR":
    print("Your average grade was out of range, please reload and try again")