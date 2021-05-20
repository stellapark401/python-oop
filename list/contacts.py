class Contacts(object):
    def __init__(self, name, phone, mail, address, num):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.address = address
        self.num = num

    def print_contact(self):
        print('*'*20)
        print('이름:', self.name)
        print('전화번호:', self.phone)
        print('이메일 주소:', self.mail)
        print('주소:', self.address)
        print('회원번호:', self.num + 1)

    @staticmethod
    def main():
        c = list()
        opt = 1

        while opt:
            name = input('이름을 입력하세요: ')
            phone = input('전화번호를 입력하세요: ')
            mail = input('이메일 주소를 입력하세요: ')
            address = input('주소를 입력하세요: ')
            c.append(Contacts(name, phone, mail, address, len(c)))
            choice = int(input('정보를 출력하고 종료하시려면 1\n정보를 추가 입력하시려면 2\n정보를 삭제하시려면 3\n종료는 0을 입력해주세요'))
            if choice == 1:
                for i in c:
                    Contacts.print_contact(i)
            elif choice == 2:
                continue
            elif choice == 3:
                del c[(int(input('삭제할 번호를 입력하세요: ')) - 1)]
            elif choice == 0:
                opt = 0
            else:
                print('잘못된 입력입니다.')
                continue


Contacts.main()

