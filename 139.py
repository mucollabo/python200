f = open('stockcode.txt', 'r', encoding='cp949')
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('%d %s' %(line_num+1, line), end='')
f.close()
# print(lines)