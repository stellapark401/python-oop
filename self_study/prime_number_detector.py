class PrimeNumberDetector(object):
    @staticmethod
    def find_divisor(pnd):
        cnt = 0
        for i in range(pnd):
            if pnd % (i + 1) == 0:
                cnt += 1
        return cnt

    @staticmethod
    def is_it_prime(cnt):
        if cnt == 1:
            return '1'
        elif cnt == 2:
            return 'prime number'
        else:
            return 'composition number'

    @staticmethod
    def pn_counter(num):
        cnt = 0
        for i in range(num):
            if PrimeNumberDetector.is_it_prime(PrimeNumberDetector.find_divisor(i + 1)) == 'prime number':
                cnt += 1
            print(f'소수는 총 {cnt}개 입니다.')

    @staticmethod
    def main():
        while True:
            mn = int(input('-소수찾기\t1\n-소수갯수\t2\n-종료\t\t0'))
            if mn == 1:
                cnt = PrimeNumberDetector.find_divisor((int(input('자연수를 입력해주세요: '))))
                print(f'The number is {PrimeNumberDetector.is_it_prime(cnt)}.')
            elif mn == 2:
                PrimeNumberDetector.pn_counter(int(input('자연수를 입력해주세요: ')))
            elif mn == 0:
                break


PrimeNumberDetector.main()
