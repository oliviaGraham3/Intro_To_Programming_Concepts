print("Olivia Graham")
#Use '#' to make comments
name = "Violet" #no var or let?? I kinda hate this.

#int, double (stores 2x positions than float), float(only 7 points of accuracy), string, char(a lone character), boolean are data types
#AGAIN NO SPECIFICATION

age = 10
temperature = 63.1 #optimized as float as much as possible

#Types of printing
print("I am {} years old, and the temperature is {} degrees".format(age, temperature))
#Curly brackets r placeholders

#input
brotherName = input("What is your name?\n")
print("The brothers name is ", brotherName)
# \t = tab \s = space \n = new line

brotherAge = int(input("What is your favorite age?\n")) #Auto takes it as a string, have to specify if you want anything else, in this case int.
print(brotherAge)

#Uh oh. Math.
total = 52 + 78
print(total)

#Uh oh. VARIABLES IN MATH
agesTotal = brotherAge + age
print(agesTotal)

#Every time i get reminded modulus exists I cry. I cry often.
modulusTotal = 5 % 2
print(modulusTotal)