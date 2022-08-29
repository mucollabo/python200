from random import shuffle
from time import sleep

gamenum = input('연금복권 구입 갯수를 입력하세요:')
print('')

if int(gamenum) >= 1 and int(gamenum) <= 5:
    jo = [y + 1 for y in range(5)]
    # print('preJo', jo)
    joret = []

    for k in range(int(gamenum)):
        shuffle(jo)
        # print('jo : ', jo)
        jonum = jo.pop()
        # print('jonum : ', jonum)
        joret.append(jonum)
        # print('joret : ', joret)

    for i in range(int(gamenum)):
        balls = [x for x in range(10)]
        ret = []

        for j in range(6):
            shuffle(balls)
            # number = balls.pop()
            ret.append(balls[j])
        # ret.sort()
        print('연금복권번호[%d조]:' % (joret[i]), end='')
        print(ret)
        sleep(1)
else:
    print('1부터 5사이의 숫자를 입력해 주세요.')

