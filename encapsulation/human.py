class Human():
    def __init__(self, name, age, sex):
        print('응애응애')
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human('모름', 00, '모름')
areum.setInfo('조아름', 25, '여자')
areum.who()