class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code


    @staticmethod
    def main():
        slst = list()
        while True:
            choice = int(input('입력: 1\n종료: 0'))
            if choice == 1:
                name = input('종목명: ')
                code = int(input('종목코드: '))
                slst.append(Stock(name, code))
            elif choice == 0:
                break
            else:
                print('잘못된 입력입니다.')


Stock.main()
