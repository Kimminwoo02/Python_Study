"""
응용문제

"""

'''
1부터 5사이에 전재하는 모든 정수를 역순으로 출력하는 프로그램을 구현하세요.
'''

# for i in range(5,0,-1):
#     print(i)


'''
사용자로부터 임의의 양수를 하나 입력받은 뒤 1부터 입력받은 양수까지 모든 정수의 합계를 출력하는 프로그램 구현

'''

# i = int(input("임의의 양수를 입력해주세요.:"))
# sum = 0
# if i <=0:
#     print("해당값은 0보다 작거나 같습니다.")
# else:
#     for num in range(1,i+1):
#         sum += num
#     print(f'1부터{i}까지의 합계는 {sum}입니다.')
#

'''
사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 그 숫자마늠 '과일이름'을 받아 'basket'에 저장하는 프로그램을 구현하세요.
예시
몇 개의 과일을 보관할까요?3
1번쨰 과일을 입력하세요 >>> 사과
2번째 과일을 입력하세요 >>> 바나나
3번째 과일을 입력하세요 >>> 체리
입력받은 과일들은 [사과,바나나,체리]입니다.
# '''
# i = int(input("몇 개의 과일을 보관할까요??:"))
# basket = []
# for number in range(1,i+1):
#     fruit = input(f'{number}번째 과일을 입력하세요:')
#     basket.append(fruit)
# print(f'입력받은 과일들은{basket}')


'''
중간고사 성적이 나왔다
한 반에 10명이 있고 각 학생의 국어점수를 번호순으로 나열하면 
다음과 같다
[99,78,100,91,81,85,54,100,71,50]
100점을 받은 학생의 점수를 제외한 나머지 학생들의 점수를 5점씩 증가시킨
'score'리스트를 생성하고 출력하는 프로그램을 구현하시오
단 증가된 점수가 100점이 초과되지 않도록 처리하시오
#
'''
# exam = [99,78,100,91,81,85,54,100,71,50]
# score= []
# for i in exam:
#     if (i+5) > 100:
#         score.append(100)
#     else:
#         score.append(i+5)
# print(score)

'''
1부터 99사이의 모든 정수를 대상으로 369 게임의 결과를 출력하는 프로그램을 구현해라
* 3의 배수를 찾는게 아니다. 
* 십의 자리와ㅓ 일의 자리를 분리해서 생각해봐야된다.
십의 자리 = num // 10
일의 자리 = num % 10
'''
# s= ''
# for i in range(1,100):
#     tens = 0
#     units = 0
#     clap=''
#     if i > 10 :
#         tens = (i // 10 ) % 3 == 0
#         if i % 10 != 0:
#             units= (i % 10) % 3== 0
#
#         if tens:
#             clap += '짝'
#         if units:
#             clap += '짝'
#          if not tens and not units:
#              clap =str(i)
#
#
#     else:
#         units = ( i % 3 == 0 )
#         if units:
#             clap += '짝'
#         if not units:
#             clap += str(i)
#
#     if i % 10 ==0:
#         s += f'{clap}\n'


'''
비밀번호 입력받아서 사용 가능한 비밀번호인지 불가능한지 판단하는 프로그램!
조건
1. 숫자와 문자 포함
2. 같은 숫자, 문자가 2개 이하여야 된다.

불가능 조건
1. 숫자와 문자 둘다 없다.
2. 같은 숫자 문자가 3개 이상
'''

pwd = input("비밀번호를 입력하세요:")
d = {}
ch_count = 0  # 문자열
num_count = 0 # 숫자
overlap_pwd = 0 # 중복

for ch in pwd:
   if ch not in d:
       d[ch] = 1
   else:
       d[ch] = d[ch] + 1

   if ch.isalpha():
       ch_count += 1
   elif ch.isnumeric():
       num_count +=1

print(d)

for i in d:
    if d[i] >= 3:
        overlap_pwd +=1
if ch_count > 0 and num_count > 0 and overlap_pwd == 0:
    print('가능')
else:
    print('불가능')