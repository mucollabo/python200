spos = 105
size = 500

f = open('stockcode.txt', 'r', encoding='cp949')
h = open('stockcode_part.txt', 'w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close()
f.close()