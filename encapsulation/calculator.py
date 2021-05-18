class Calculator:
    third = 77

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        if self.first > self.second:
            result = self.first - self.second
        else:
            result = self.second - self.first
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        if self.first > self.second:
            result = self.first / self.second
        else:
            result = self.second / self.first
        return result

    def reset(self, third):
        self.third = third
    @staticmethod
    def main():
        c = Calculator(int(input('첫번째 수 입력: ')), int(input('두번째 수 입력: ')))
        print(f'{c.first} + {c.second} = {c.add()}')


class adCal(Calculator):
    def __init__(self, first, second):
        self.first = first
        self.second = second
'''
if __name__ == '__main__':
    c = Calculator(1,2)
    print(c.first)
    print(c.second)
    print(c.first + c.second)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
    c.setdata(3, 9)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
    print(c.third)
    c.reset(44)
    print(c.third)'''
Calculator.main()