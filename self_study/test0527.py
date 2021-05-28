import pandas as pd


class Trial(object):
    variable = '공유'

    @staticmethod
    def main():
        trial = 'static 도 local var. 호출이 가능한가욥'
        print(trial)
        pass


a = Trial()
b = Trial()
print(a.variable)
print(b.variable)
a.variable = 'a'
b.variable = 'b'
print(a.variable)
print(b.variable)
Trial.variable = 'c'
print(a.variable)
print(b.variable)
dt = {'1': (1, 2, 3), '2': (4, 5, 6)}
df = pd.DataFrame(dt)
print(df)
print([str(2 * x - 2) for x in range(12) if x % 3 == 2])
dt = {(1, 2): 1, (3, 4): 2, (5, 6): 3}
for i in dt:
    print('가능', i[0])
print(list('hello'))
hello = list('hello')
print(hello)
print(list([1, 2, 3]))
tp = (1, 2, 3)
no_connotation = [tp]
print(type(no_connotation))
print(no_connotation)
df_src_col = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
df_src_ind = ['A', 'B', 'C']
df = pd.DataFrame(df_src_col, df_src_ind)
print(df)
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], df_src_ind)
print(df)
df_src = {'a': [(1, 2), (3, 4)], 'b': [(5, 6), (7, 8)], 'c': [(9, 10), (11, 12)]}
df = pd.DataFrame(df_src, index=['A', 'B'])
print(df)
# df.to_csv('./data.trial.csv')
try:
    a = [1, 2]
    4/0
    print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)
