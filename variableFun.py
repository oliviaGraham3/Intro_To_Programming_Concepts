firstNumFirstQ = int(input("What is your first number for the first question?\n"))
secondNumFirstQ = int(input("What is your second number for the first question?\n"))

firstNumSecondQ = int(input("What is your first number for the second question?\n"))
secondNumSecondQ = int(input("What is your second number for the second question?\n"))

firstNumThirdQ = int(input("What is your first number for the third question?\n"))
secondNumThirdQ = int(input("What is your second number for the third question?\n"))

firstNumFourthQ = int(input("What is your first number for the fourth question?\n"))
secondNumFourthQ = int(input("What is your second number for the fourth question?\n"))

firstNumFiveQ = int(input("What is your first number for the fifth question?\n"))
secondNumFiveQ = int(input("What is your second number for the fifth question?\n"))

firstNumSixQ = int(input("What is your first number for the sixth question?\n"))
secondNumSixQ = int(input("What is your second number for the sixth question?\n"))

questionOne = firstNumFirstQ * secondNumFirstQ
print("The answer to your query is: ", questionOne , "\n")

questionTwo = firstNumSecondQ / secondNumSecondQ
print("The answer to your query is: ", questionTwo , "\n")

questionThree = firstNumThirdQ // secondNumThirdQ #shhh I don't know if this is the right way but it gets the right answer
print("The answer to your query is: ", questionThree , "\n")

questionFour = firstNumFourthQ % secondNumFourthQ
print("The answer to your query is: ", questionFour , "\n")

questionFive = firstNumFiveQ + secondNumFiveQ
print("The answer to your query is: ", questionFive , "\n")

questionSix = firstNumSixQ - secondNumSixQ
print("The answer to your query is: ", questionSix , "\n")

print("Olivia Graham")