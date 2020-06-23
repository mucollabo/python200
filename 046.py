from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse

sleep(3)
txt1 = mylib.add_txt('나는', '파이썬이다')
print(txt1)
txt2 = reverse(1, 2, 3)
print(txt2)