class GradeTest:
    def __init__(self, kor, eng):
        self.kor = kor
        self.eng = eng

    def sum(self):
        return self.kor + self.eng

    def avg(self):
        return self.sum() / 2

    def getGrade(self):
        score = int(self.avg())
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def main():
        gt = GradeTest(int(input('국어 점수: ')), int(input('수학 점수: ')))
        print(f'총점: {gt.sum()}')
        print(f'평균: {gt.avg()}')
        print(f'학점: {gt.getGrade()}')


GradeTest.main()
