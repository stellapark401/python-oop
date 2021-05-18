class CalculatorStatic(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.second != 0:
            return self.first / self.second
        else:
            return 'This calculation can not be done.'

    @staticmethod
    def mAdd():
        cs = CalculatorStatic(3, 0)
        print(cs.add())

    @staticmethod
    def mSub():
        cs = CalculatorStatic(3, 0)
        print(cs.sub())

    @staticmethod
    def mMul():
        cs = CalculatorStatic(3, 0)
        print(cs.mul())

    @staticmethod
    def mDiv():
        cs = CalculatorStatic(3, 0)
        print(cs.div())



if __name__ == '__main__':
    CalculatorStatic.mAdd()
    CalculatorStatic.mSub()
    CalculatorStatic.mMul()
    CalculatorStatic.mDiv()
