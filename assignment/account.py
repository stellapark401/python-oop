import random


class Account(object):
    account_count = 0

    def __init__(self, name, balance):
        self.bank = 'sc은행'
        self.name = name
        self.balance = balance
        self.account_number = str(random.randint(100, 999)) + '-' + str(random.randint(10, 99)) + '-' + str(random.randint(100000, 999999))
        Account.account_count += 1

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount}원이 {{{self.name}}}님의 계좌에 입금되었습니다.')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount}원이 {{{self.name}}}님의 계좌에서 출금되었습니다.')
        else:
            print('잔액이 부족합니다.')

    def print_account(self):
        print(f'은행이름: {self.bank}\n예금주: {self.name}\n계좌번호: {self.account_number}\n잔고: {self.balance}원')

    def deposit_history(self):
        pass

    def withdraw_history(self):
        pass

    @staticmethod
    def main():
        ac = list()

        def feed_in():
            name = input('이름: ')
            balance = int(input('잔액: '))
            return name, balance

        while True:
            choice = int(input('계좌 등록:\t1\n계좌 출력:\t2\n계좌 개수:\t3\n입금:\t\t4\n출금:\t\t5\n종료:\t\t0\n을 입력해주세요'))
            if choice == 1:
                ac.append(Account(*feed_in()))
            elif choice == 2:
                if len(ac):
                    for i in ac:
                        print('*' * 20)
                        i.print_account()
                    print('*' * 20)
                else:
                    print('등록된 계좌가 없습니다.')
            elif choice == 3:
                print('등록된 계좌 개수:', Account.account_count)
            elif choice == 4:
                name = input('예금주: ')
                amount = int(input('입금액: '))
                for i in ac:
                    if name == i.name:
                        i.deposit(amount)
                    else:
                        continue
            elif choice == 5:
                name = input('예금주: ')
                amount = int(input('츨금액: '))
                for i in ac:
                    if name == i.name:
                        i.withdraw(amount)
                    else:
                        continue
            elif choice == 0:
                break
            else:
                print('잘못된 입력입니다.')


Account.main()
