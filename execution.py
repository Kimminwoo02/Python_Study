import random
import time

pot = list(range(1,46))
jackpot=[]

for i in range(1,7):
    random.shuffle(pot)
    num = pot[-1]
    print(f'{i}번째 당첨번호는 {num}입니다.')
    jackpot.append(num)
    time.sleep(2)
jackpot.sort()
print(f'이번 당첨번호는{jackpot}입니다.')