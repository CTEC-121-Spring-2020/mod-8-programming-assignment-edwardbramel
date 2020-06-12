# Module 8
#   Programming Assignment 11
#     Prob-1.py

# Your code below

''''
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
'''
# testing

# this is what you want


class car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def setmake(self, make):
        self._make = make

    def getmake(self):
        return self._make

    def setmodel(self, model):
        self._model = model

    def getmodel(self):
        return self._model

    def setyear(self, year):
        self._year = year

    def getyear(self):
        return self._year


def test():
    carlot = []
    carlot.append(car("ford", "gt", "2007"))
    carlot.append(car("chevy", "torndado", "2002"))
    carlot.append(car("subaru", "wrx", "2009"))
    carlot.append(car("nissian", "gtr", "2017"))
    carlot.append(car("toyota", "86", "1990"))
    for element in carlot:
        print(element.getmake())
        print(element.getmodel())
        print(element.getyear())


if __name__ == "__main__":
    test()
