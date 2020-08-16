f = open('stockcode.txt', 'r', encoding='cp949')
h = open('stockcode_copy.txt', 'w')

data = f.read()
h.write(data)

f.close()
h.close()
