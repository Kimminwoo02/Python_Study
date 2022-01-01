"""
응용문제!

"""
import random
import time

'''
1. 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요!

지시사항
-1 ~ 45 사이의 모든 정수를 순서대로 pot 리스트에 저장합니다.
-다음 과정을 6번 반복합니다!
    -pot 리스트를 무작위로 섞어줍니다.
    -pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
    -2초동안 잠시 멈춥니다!
-jackpot 리스트의 모든 요소를 오름차순 정렬합니다
-jackpot 리스트의 모든 요소를 출력합니다!

'''
from random import *
from time import *

pot = list(range(1,46))
jackpot = []

for i in range(1,7):
    random.shuffle(pot)
    num = pot[-1]
    print(f'{i}번째 당첨번호는{num}입니다.')
    jackpot.append(num)
    time.sleep(2)

jackpot.sort()
print(f'이번 당첨번호는{jackpot}입니다.')

'''
다음 지시사항에 따라 up down 게임을 구현하세요
1~100 사이의 정수중 하나를 임의로 생성하면 사용자는 그 숫자를 맞힐 때까지 앖을 예상하여 입력합니다!
-사용자가 입력한 값이 정답보다 작으면 up, 크면 down을 출력합니다!
이때 소수 아래 값은 내림 처리하여 정수로 출력!

Ex) 어떤 값일까요?  50
Down
어떤 값일까요 25
up
어떤 값일까요? 35
down
어떤 값일까요? 27
정답입니다!
18초 만에 성공하였습니다

'''
import math
print('up,down을 시작합니다!')
num =random.randint(1,100)
start = time()


while True:
    input_num = int(input('어떤 값일까요?:'))
    if input_num == num:
        print('정답입니다!')
        end = time()

        print(f'{math.floor(end -  start)}초 만에 성공하였습니다.')
        break
    elif input_num < num:
        print('Up')
    elif input_num > num:
        print('Down')

'''

다음 지시사항에 따라 문제를 만들어보세요!
-롱소드, 숏소드 두개의 무기가 담긴 dict 타입의 변수를 선언하세요!
-다음 조건이 만족되면 반복문을 종료하세요!
    -사용자가 강화를 원하지 않는다!
    -더 이상 강화할 수 있는 무기가 없다!
-강화를 시작하면 1~3 초 사이의 시간으로 잠시 일시정지!
-50% 확률로 강화가 성공/실패 하게 하세요!
-성공과 실패시 다음과 같은 작업을 해주세요!
    -성공
        현재 선택된 무기의 강화수치를 +1 해주세요!
    -실패
        강화실패.. 띄우고 해당 무기를 dict 변수에서 없에주세요!
'''

weapon= {
    '롱소드': 0 ,
    '숏소드': 0
}

while True:
    if len(weapon)>0:
        choice_weapon = input(f'강화하고 싶은 무기를 선택하세요{list(weapon.keys())}')

        if choice_weapon in weapon:
            is_reinforece = input(f'{choice_weapon}{weapon}'
                                  f'({weapon[choice_weapon]}) 무기를 선택하셨습니다.'
                                  f'강화하시겠습니까?(Y/N) >>')
            if is_reinforece.upper() =='Y':
                print('강화를 시작합니다!')
                time.sleep(random.randint(1,3))
                if random.random() <0.5:
                    print('강화 성공!')
                    weapon[choice_weapon] += 1
                else:
                    print('강화실패...')
                    del weapon[choice_weapon]
            elif is_reinforece.upper() =='N':
                print('강화를 종료합니다!')
            else:
                print('다시 입력해주세요.')
                continue
    else:
        print('강화할 수 있는 무기가 없습니다!')
        break