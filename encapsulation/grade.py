class Grade:
    def __int__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    '''
    동일한 구조로 다른 클래스명은 되는데, Grade가 생성시 takes no arguments...  뭔가 내부에서 꼬인 것 같다.
    @staticmethod
    def sum():
        g = Grade(100, 100, 97)
        print(g.kor + g.eng + g.math)

    @staticmethod
    def sum():
        g = Grade(int(input('국어 점수: ')), int(input('영어 점수: ')), int(input('수학 점수: ')))
        return g.kor + g.eng + g.math

    @staticmethod
    def avg():
        g = Grade(100, 100, 97)
        return g.kor + g.eng + g.math / 3
'''

