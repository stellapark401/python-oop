class Person(object):
    def __init__(self, name, yearofbirth, address):
        self.name = name
        self.yearofbirth = yearofbirth
        self.address = address

    def age(self):
        return 2021 - self.yearofbirth + 1

    @staticmethod
    def main():
        p = Person(input('이름: '), int(input('출생년도: ')), input('주소: '))
        print(f'{"회원가입을 축하합니다.":*^20}')
        print(f'{p.name}님의 나이: {p.age()}')
        print(f'{p.name}님의 주소: {p.address}')
        print('*' * 26)


Person.main()
