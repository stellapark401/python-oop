class Grade:
    (kor, eng, math) = (0, 0, 0)

    def set_grade(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

if __name__ == '__main__':
    g = Grade()
    g.set_grade(100, 100, 97)
    print(g.sum())
    h = Grade()
    print(h.sum())
    print(g.avg())
