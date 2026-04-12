amntOwed = 0
drinkGet = ""

class Drinks:
    def __init__(self, drinkName, price, location):
        self.drinkName = drinkName
        self.price = price
        self.location = location

drink1 = Drinks("Sprite", 2.5, "1A")
drink2 = Drinks("Coke", 2.5, "2A")
drink3 = Drinks("Gatorade", 3.0, "3A")
drink4 = Drinks("Monster Energy", 4.5, "1B")
drink5 = Drinks("Iced Tea", 2.5, "2B")
drink6 = Drinks("Water", 2.0, "3B")

print("The drinks available are:\n Sprite (1A)   Coke (2A)   Gatorade (3A)\n Monster Energy (1B)  Iced Tea (2B)  Water (3B)")

while (True):
    userChoice = input("Choose the drink you would like based on the number/letter combination the the right of your choice: ")
    match userChoice:
        case "1A":
            amntOwed = drink1.price
            drinkGet = "Sprite"
        case "2A":
            amntOwed = drink2.price
            drinkGet = "Coke"
        case "3A":
            amntOwed = drink3.price
            drinkGet = "Gatorade"
        case "1B":
            amntOwed = drink4.price
            drinkGet = "Monster Energy"
        case "2B":
            amntOwed = drink5.price
            drinkGet = "Iced Tea"
        case "3B":
            amntOwed = drink6.price
            drinkGet = "Water"
    while True:
        dollarGiven = round(float(input("Please enter a number greater than 0.009 to represent money paid to The Machine: \n")), 2)

        if dollarGiven >= amntOwed:
            print("Thank you, here's your drink \n")
            break
        elif dollarGiven <= 0 or dollarGiven == "":
            print("You have not entered a valid amount, please try again\n")
            break
        elif dollarGiven < amntOwed:
            print("You still owe ", amntOwed - dollarGiven, ", please enter the rest")
            amntOwed = amntOwed - dollarGiven

    amntOwed = 0
    drinkGet = ""