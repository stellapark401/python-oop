def bmi_function(mass, height):
    return mass / (height/100)**2


class Bmi(object):
    def __init__(self, mass, height):
        self.mass = mass
        self.height = height

    def score(self):
        return self.mass / ((self.height / 100) ** 2)

    def print_it(self):
        result = self.mass / ((self.height / 100) ** 2)
        print('Your bmi score is %.2f(kg/m^2).' % result)

    def assessment(self):
        if self.score() >= 30:
            return 'obese'
        elif self.score() >= 25:
            return 'overweight'
        elif self.score() >= 18.5:
            return 'normal'
        else:
            return 'underweight'

    @staticmethod
    def main():
        bm = Bmi(int(input('몸무게(kg): ')), int(input('키(cm): ')))
        print(f'{bm.height}cm의 {bm.mass}kg인 당신의 BMI는 {bm.score():0.2f}입니다.')
        print(f'According to BMI assessment you are {bm.assessment()}, Be healthy.')

'''
if __name__ == '__main__':
    b = Bmi(60.5, 161)
    b.print_it()
    print('%.2f' % bmi_function(60, 161))
'''
Bmi.main()