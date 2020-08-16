bufsize = 1024
f = open('/Users/charles/Pictures/wallpaper/rishi-jhajharia-1CkSNmbT7J0-unsplash.jpg', 'rb')
h = open('./myimages/img_sample_copy.jpg', 'wb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)

f.close()
h.close()