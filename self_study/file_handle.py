# fh = open('sample_text.txt', 'a')
# fh.write('첫 줄 적어봅니다.')
# fh.write('두번째 줄 덧붙입니다.')
# fh.write('새로운 줄에 덧붙입니다.')
# fh.write('\n\n\n\t\t white space here\n\n\n')
'''
for i in range(10):
    fh.write(f' saying hello: {i + 1}times\n')
'''
fh = open('sample_text.txt', 'r')
print(len(fh.read()))
print(type(fh.read()))
fh.close()
