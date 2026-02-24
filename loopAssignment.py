menu = ["Taco", "Burrito", "Nachos", "Soft Drink", "Quit"]

print("Welcome to Taco Palace!  Please view the menu below and make a selection \n")

def makingOrder():
    orderInput = 0
    totalPrice = 0
    ordersPlaced = []

    while orderInput != 5:
        print("Palooza Menu")
        x = 1
        for i in range(0, len(menu)):
            print(x, ": ", menu[i])
            x += 1

        orderInput = int(input("User Input: "))
        if orderInput == 1:
            totalPrice += 10.00
        elif orderInput == 2:
            totalPrice += 10.00
        elif orderInput == 3:
            totalPrice += 7.00
        elif orderInput == 4:
            totalPrice += 4.00

        print("You selected " , menu[orderInput - 1], "\n")
        ordersPlaced.append(menu[orderInput - 1])
    ordersPlaced.pop(len(ordersPlaced) - 1)
    joinStatement = ", ".join(ordersPlaced)

    print("You ordered ", joinStatement, ". Your total is $", totalPrice)
makingOrder()