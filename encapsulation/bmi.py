class Bmi():
    def __init__(self, mass, height):
        self.mass = mass
        self.height = height

    def printit(self):
        result = self.mass / ((self.height / 100) ** 2)
        print('Your bmi score is %.2f(kg/m^2).' % result)


if __name__ == '__main__':
    b = Bmi(60.5, 161)
    b.printit()