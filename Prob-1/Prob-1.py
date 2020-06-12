# Module 8
#   Programming Assignment 11
#     Prob-1.py

# Your code below


class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


def testcar():
    carlot = []
    howmany = int(input("how many cars you have on the lot? "))

    for i in range(howmany):
        make = input("what is the make? ")
        model = input("what is the model? ")
        year = input("what year is it? ")
        car = Cars(make, model, year)
        carlot.append(car)
        print("the make for the car is", make,
              "and its a", model, "model, and its made in the year", year)


testcar()
# testing
'''
# this is what you want


class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


def carlot():
    car1make = "ford"
    car1model = "gt"
    car1year = "2007"
    print("the first car is,", car1make, "the model of it is,",
          car1model, " and the year for car 1 is", car1year)


carlot()
'''
