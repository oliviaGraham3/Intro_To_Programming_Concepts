import math


def areaCirc(radius):
    area = math.pi * (radius ** 2)
    return area

def taxes(money , taxRate):
    total = money + money * (taxRate / 100)
    return total

def temp(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius

print(round(areaCirc(int(input("Enter radius: \n"))), 2)) #took me like 5 tries but I GOT IT W/O MAKING A NEW VARIABLE YEAHHH

print(taxes(int(input("Enter money: \n")) , int(input("Enter tax rate as a percent: \n")) ))
# no one does it like i do, its uglier and also more difficult this way and it will never be done like this outside of basic assignments

print(temp(int(input("Enter temperature in fahrenheit: \n"))))