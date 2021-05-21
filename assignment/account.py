import random


class Account(object):
    account_count = 0

    def __init__(self, name, balance):
        self.BANK = 'SC은행'
        self.name = name
        self.balance = balance
        self.account_number = Account.create_account()
        self.deposit_count = 0
        self.withdraw_count = 0
        self.hist = dict()
        '''hist = { 입출금 횟수 : ( 이전금액, 금액, 잔액, (입금: 1,출금: 0) ) }'''
        Account.account_count += 1

    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''
    @staticmethod
    def create_account():
        return str(random.randint(100, 999)) + '-' + str(random.randint(10, 99)) + '-' + str(random.randint(100000, 999999))

    def deposit(self, amount):
        if amount:
            prev = self.balance
            self.balance += amount
            print(f'{amount}원이 {{{self.name}}}님의 계좌에 입금되었습니다.')
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = 1.01 * self.balance
                print(f'입금 횟수가 5회가 되서 {{{self.name}}}님의 계좌에 이자가 입금되었습니다.')
            else:
                pass
            self.deposit_history(amount, prev)
        else:
            print('입금할 금액이 없습니다.')

    def withdraw(self, amount):
        if self.balance >= amount:
            prev = self.balance
            self.balance -= amount
            print(f'{amount}원이 {{{self.name}}}님의 계좌에서 출금되었습니다.')
            self.withdraw_count += 1
            self.withdraw_history(amount, prev)
        else:
            print('잔액이 부족합니다.')

    def display_info(self):
        print(f'은행이름: {self.BANK}\n예금주: {self.name}\n계좌번호: {self.account_number}\n잔고: {self.balance}원')

    def deposit_history(self, amount, prev):
        self.hist[self.deposit_count + self.withdraw_count] = (prev, amount, self.balance, 1)

    def withdraw_history(self, amount, prev):
        self.hist[self.deposit_count + self.withdraw_count] = (prev, amount, self.balance, 0)

    def display_history(self):
        for i in self.hist.keys():
            print('*' * 70)
            if self.hist[i][3]:
                print(f'입금전:\t{self.hist[i][0]}원\t입금액:\t{self.hist[i][1]}원\t잔액:\t{self.hist[i][2]}원')
            else:
                print(f'출금전:\t{self.hist[i][0]}원\t출금액:\t{self.hist[i][1]}원\t잔액:\t{self.hist[i][2]}원')

    @staticmethod
    def main():
        ac = list()

        def feed_in():
            feed_name = input('이름: ')
            balance = int(input('잔액: '))
            return feed_name, balance

        while True:
            choice = int(input('계좌 등록:\t1\n계좌 출력:\t2\n계좌 개수:\t3\n입금:\t\t4\n출금:\t\t5\n입출금 내역:\t6\n거대 고객:\t7\n종료:\t\t0\n을 입력해주세요'))
            if choice == 1:
                ac.append(Account(*feed_in()))
            elif choice == 2:
                if len(ac):
                    for i in ac:
                        print('*' * 20)
                        i.display_info()
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
            elif choice == 6:
                name = input('예금주: ')
                for i in ac:
                    if name == i.name:
                        i.display_history()
                    else:
                        continue
            elif choice == 7:
                cnt = 0
                for i, j in enumerate(ac):
                    if j.balance >= 1000000:
                        print('=' * 20)
                        j.display_info()
                        cnt += 1
                    else:
                        continue
                if cnt:
                    print(f'100만원 이상의 잔액을 보유한 거대 고객님의 수: {cnt}명')
                else:
                    print('100만원 이상의 잔액을 보유한 고객님이 없습니다.')
            elif choice == 0:
                break
            else:
                print('잘못된 입력입니다.')


Account.main()
