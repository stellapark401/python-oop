class TupleTest(object):
    def __init__(self, tup):
        self.name = tup[0]
        self.age = tup[1]

    def print_tpl(self):
        print(f'이름: {self.name}\n나이: {self.age}')

    @staticmethod
    def main():
        tt = list()

        def feed_in():
            name = input('이름: ')
            age = input('나이: ')
            return name, age
        while True:
            choice = int(input('입력: 1\n출력: 2\n종료: 0'))
            if choice == 1:
                tt.append(TupleTest(feed_in()))
            elif choice == 2:
                for i in tt:
                    i.print_tpl()
            elif choice == 0:
                break
            else:
                print('잘못된 입력입니다.')


TupleTest.main()
