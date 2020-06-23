import time
import mylib
import mypackage.mylib

time.sleep(3)
txt1 = mylib.add_txt('나는', '파이썬이다')
print(txt1)
time.sleep(3)
txt2 = mypackage.mylib.reverse(1, 2, 3)
print(txt2)