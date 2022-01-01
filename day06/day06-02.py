'''
사용자로부터 5개의 양의 정수를 받아
그 합계를 구하는 프로그램!

만약 0 이하의 값이 입력되면 사용자에게 재 입력을 요구 받으세요!
  1번째 정수를 입력하세요
  .
  .
  .
'''

count = 0
total = 0

while count < 5:
    n = int(input(f"{count+1}번째 정수를 입력하세요 >>>"))
    if n <= 0 :
        print('0 이하의 수는 출력할 수 없습니다.')
        continue
    total += n
    count += 1
print(f'합계는 {total} 입니다.')


'''
현재 만원을 가지고 있다!
얼마를 사용할 것인지 반복해서 입력 받아서 만원을 다 사용하시오
0 이하의 금액은 사용 불가능이며 현재 가지고 있는 금액보다 더 큰 금액도 사용 불가!
무한루프랑 break 이용

예시
현재 10000원이 있습니다.
사용할 금액 입력 5000
현재 5000원이 있습니다.
'''
"""
money = 10000

while True:
    if money != 0:
        print(f'현재 {money}원이 있습니다.')
        pay = int(input('사용할 금액 입력:'))

        if pay <= 0:
            print('0이하의 금액은 사용할 수 없습니다.')
        elif (money - pay) < 0:
            print(f'{pay - money}원이 부족합니다.')
        elif (money - pay) == 0:
            print('현재 0 원이 있습니다.')
            break
        else:
            money -= pay
            continue

"""
'''
평점을 입력받아 별을 출력!

star = ''
while True:
    score = int(input("영화의 평점을 입력하세요!:"))
    if score <=0 or score >= 6:
        print('평점은 1~5 사이만 입력가능')
    else:
        for i in range(score):
            star += '★'
        break
print(f'평점:{star}')

'''




'''

책 예제 
저장된 비밀번호를 맞히는 프로그램을 구현하세요!
저장된 비밀번호는 qwerty이고 최대 5번 시도 가능!
5번 이내에 비밀번호를 맞히면 비밀번호를 맞혔습니다! 를출력
그렇지 않으면 '비밀번호 입력 횟수를 초과했습니다'를 출력

'''
pwd ='qwerty'
count = 0
while True:
    if count == 0 :
        print('비밀번호 입력 횟수를 초과했습니다.')
        break
    else:
        input_pwd = input("비밀번호를 입력하세요 >>>")
        if pwd == input_pwd:
            print('비밀번호를 맞췄습니다.')
            break
        else:
            count -= 1

'''

책 예제 
다음 조건을 만족하는 구구단을 출력하세요!
-짝수인 (2,4,6,8) 단은 출력하지 말고 줄넘김만 추가
- 각 단까지만 출력하는데, 3단이면 3x3 까지 5단이면 5x5까지만 출력
-
'''
for x in range(2,10):
    for y in range(1,x+1):
        if x % 2 == 0:
            print("\n")
            break
        else:
            print(f'{x} X {y} = {x*y}')


