"""
메소드 문제풀이!
"""

'''
예제 : basket 이라는 10가지의 과일이 들어가있는 리스트 변수가 있습니다.
pop 메소드를 이용해서 과일을 하나씩 꺼내고 basket 변수를 비워보세요

basket = 사과 ,바나나 사과 체리 망고 망고 망고 사과 수박
'''
basket = ['사과','바나나','사과','체리','망고','망고','망고','사과','수박','메론']
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket.pop())
print(basket)

#이걸 포문으로 쓰면?!

basket_len = int(len(basket))
for i in range(basket_len):
    print(basket.pop())
'''
1. 우리나라의 전화번호는 지역번호-국번-가입자개별번호 형식입니다.
어떤 형식의 전화번호를 입력하더라도 '국번'을 추출하여 출력하는 프로그램을 구현!

'''

address = input("전화번호를 입력하세요:")
first_hyphen = address.index('-') + 1 # +1 을 안하면 프린트 결과가 두개가 똑같이 나온다. 뒤에서 부터 찾아야 되기 때문에!
two_hyphen = address.index('-',first_hyphen) # index 는 찾는거!
print(first_hyphen)
print(two_hyphen)
print(f'{address[first_hyphen:two_hyphen]}')

# 위 처럼 하면 지저분하다. 간단한 방법이 있다
# Split 이용!

splits = address.split('-') # 02,1234,5678 리스트 생성!
print(f'{splits[1]}')

'''
2. 숫자 3자리 - 숫자 2자리 - 숫자 5자리 형식 의 사업자 등록번호를
입력받아서 형식이 맞는지 점검하는 프로그램을 구현하세요
단 다음 지시사항을 모두 점검해야합니다!
지시사항 
-전체 글자수를 점검
- 모든 하이픈의 위치가 올바른지 점검합니다.
- 하이픈을 제외하면 모두 숫자인지 점검합니다.

'''

company_number = input('사업자 등록번호를입력하세요 : ')
if len(company_number) == 12:
    print("올바른 형식이 아닙니다!")
else:
    splits = company_number.split('-')
    first = splits[0]
    second = splits[1]
    third = splits[2]

    if len(first) == 3 and len(second) == 2 and len(third) == 2:
        if first.isdecimal() and second.isdecimal() and third.isdecimal():
            print('올바른 형식입니다.')
        else:
            print("올바르지 않습니다")
    else:
        print('하이픈의 위치가 알맞지 않습니다')
'''
우리 학교 성적 관리 프로그램은 다음과 같이 쉼표 로 구분된
문자열 형식으로 학생 이름과 성적이 입력됩니다.
이 데이터를 각각 name 과 score 변수에 저장하는 프로그램을 구현하세요.

값 예시
data= '"김철수",85'
'''

data = '"김철수",85'
splits = data.split(',')
name = splits[0].strip('\"')
score = splits[1]
print(f'이름은{name}이고 점수는{score}입니다.')