class Stock:
    def __init__(self, name, code, PER, PBR, dividend):
        self.name = name
        self.code = code
        self.PER = float(PER)
        self.PBR = float(PBR)
        self.dividend = float(dividend)

    def print_stock(self):
        print(f'종목명:\t\t{self.name}\n종목코드:\t{self.code}\nPER:\t\t{self.PER}\nPBR:\t\t{self.PBR}\n배당수익률:\t{self.dividend}')

    def set_PER(self, change):
        self.PER = change

    def set_PBR(self, change):
        self.PBR = change

    def set_dividend(self, change):
        self.dividend = change

    @staticmethod
    def main():
        slst = list()
        while True:
            choice = int(input('입력:\t1\n출력:\t2\n수정:\t3\n종료:\t0'))
            if choice == 1:
                name = input('종목명: ')
                code = input('종목코드: ')
                PER = float(input('PER: '))
                PBR = float(input('PBR: '))
                dividend = float(input('배당수익률: '))
                slst.append(Stock(name, code, PER, PBR, dividend))
            elif choice == 2:
                if len(slst):
                    for i in slst:
                        print('*' * 20)
                        i.print_stock()
                    print('*' * 20)
                else:
                    print('등록된 종목이 없습니다.')
            elif choice == 3:
                menu = int(input('수정\t내용\nPER:\t\t1\nPBR:\t\t2\n배당수익률:\t3'))
                if menu == 1:
                    print('*' * 20)
                    name = input('수정할 종목명: ')
                    change = float(input('수정할  PER: '))
                    for i, j in enumerate(slst):
                        if name == j.name:
                            j.set_PER(change)
                        else:
                            continue
                elif menu == 2:
                    print('*' * 20)
                    name = input('수정할 종목명: ')
                    change = float(input('수정할  PBR: '))
                    for i, j in enumerate(slst):
                        if name == j.name:
                            j.set_PBR(change)
                        else:
                            continue
                elif menu == 3:
                    print('*' * 20)
                    name = input('수정할 종목명: ')
                    change = float(input('수정할  배당수익률: '))
                    for i, j in enumerate(slst):
                        if name == j.name:
                            j.set_dividend(change)
                        else:
                            continue
                else:
                    print('잘못된 입력입니다.')
            elif choice == 0:
                break
            else:
                print('잘못된 입력입니다.')


Stock.main()
