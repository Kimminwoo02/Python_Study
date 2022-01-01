"""
break

"""

'''
1.break문
break문은 while문이나 for문과 같은 반복문을 강제로 종료하고자 할 때 사용하는 제어문입니다.
반복분 내에 break가 나타나면 곧바로 break 문이 포함된 반복문은 종료합니다.

반복문을 원하는 시점에 정확하게 반복문을 종료시키는 것은 매우 어렵다
이럴 때 사용하는 것이 break.
무한히 반복되는 무한루프로 반복문을 구성한 뒤 if 문을 이용해서 반복문을 종료시킬 
조건식을 만든 후 break 문을 사용해 반복문을 종료하면 된다!

'''
while True:
    print('x')
    while True:
        print('X')
        break

