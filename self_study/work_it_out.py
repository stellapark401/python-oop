class Wikipedia(object):
    url = ''
    instance_cnt = 0

    def __init__(self):
        self.ins_cnt = Wikipedia.instance_cnt + 1
        Wikipedia.instance_cnt += 1

    @staticmethod
    def main():
        while True:
            menu = int(input('입력\t\t1\n출력\t\t2\n종료\t\t0\n'))
            if menu == 1:
                uV = input('URL 입력: ')
                wk = Wikipedia()
                wk.url = uV
                wk.instance_cnt += 1
            elif menu == 2:
                print(f'URL: {wk.url}, the number of instances: {wk.ins_cnt}, class var.: {wk.instance_cnt}')
            elif menu == 0:
                break
            else:
                print('잘못된 입력입니다.')
                continue


Wikipedia.main()
ins1 = Wikipedia()
ins1.url = 'www.google.com'
ins1.instance_cnt = 1
ins2 = Wikipedia()
ins2.url = 'www.daum.net'
ins2.instance_cnt = 2
ins3 = Wikipedia()
ins3.url = 'www.naver.com'
ins3.instance_cnt = 1
print(ins1.url)
print(ins1.ins_cnt)
print(ins1.instance_cnt)
print(Wikipedia.url)
print(Wikipedia.instance_cnt)
print(ins2.url)
print(ins2.ins_cnt)
print(ins2.instance_cnt)
print(Wikipedia.url)
print(Wikipedia.instance_cnt)
print(ins3.url)
print(ins3.ins_cnt)
print(ins3.instance_cnt)
print(Wikipedia.url)
print(Wikipedia.instance_cnt)
