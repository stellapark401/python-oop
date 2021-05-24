a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)
a[1] = 3
print(a)
print(b)
c = list()
print(id(c))
c = a
print(id(c))
c[1] = 2
print(a)
print(c)
d, e = 1, 2
print('d: %d, e: %d' % (d, e))
d, e = e, d
print('d: %d, e: %d' % (d, e))
id_num = input('주민번호를 입력하세요(######-#######): ')
id_num = id_num.split('-')
if int(id_num[1][0]) >= 3:
    print(f'20{id_num[0]}, {id_num[1]}')
else:
    print(f'19{id_num[0]}, {id_num[1]}')
aT = 'a:b:c:d'
print(aT)
print(aT.replace(':', '#'))
at = (1, 2, 3)
at = at + (4, )
print(at)
dict_test = {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}
trial = dict_test.pop('2')
print(trial)
print(dict_test)
lst_trial = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_trial = set(lst_trial)
print(set_trial)