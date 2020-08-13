f = open('stockcode.txt', 'r', encoding='cp949')
data = f.read()
print(data)
f.close()