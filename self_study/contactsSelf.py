class ContactsSelf(object):
    def __init__(self, name, phone, mail, address, num):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.address = address
        self.num = num

    def print_contact(self):
        print('*' * 20)
        print('이름:', self.name)
        print('전화번호:', self.phone)
        print('이메일 주소:', self.mail)
        print('주소:', self.address)
        print('회원번호:', self.num + 1)

    def reset_num(self):
        self.num -= 1

    @staticmethod
    def feed_in():
        name = input('이름을 입력하세요: ')
        phone = input('전화번호를 입력하세요: ')
        mail = input('이메일 주소를 입력하세요: ')
        address = input('주소를 입력하세요: ')
        return name, phone, mail, address

    @staticmethod
    def main():
        c = list()
        while True:
            choice = int(input('정보출력:\t1\n정보입력:\t2\n삭제:\t\t3\n종료:\t\t0\n을 입력해주세요'))
            if choice == 1:
                if len(c):
                    for i in c:
                        ContactsSelf.print_contact(i)
                    print('*' * 20)
                else:
                    print('등록된 회원이 없습니다.')
            elif choice == 2:
                c.append(ContactsSelf(*ContactsSelf.feed_in(), len(c)))
            elif choice == 3:
                number_it = int(input('삭제할 회원번호를 입력해주세요: ')) - 1
                del c[number_it]
                for i in c:
                    if c.index(i) >= number_it:
                        i.reset_num()
                    else:
                        continue
            else:
                break


ContactsSelf.main()
