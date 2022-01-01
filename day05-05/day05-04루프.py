"""
비시퀸스와 for 문
"""

'''
1 for 문과 set
set은 비시퀸스 자료형이기 때문에 저장된 요소들 사이의 순서가 없다!
for 문을  이용해 저장된 요소를 부르면
순서에 상관없이 하나씩 꺼내서 사용가능하다

for 요소 in {세트}
    반복 실행문
'''

# for item in {'가위','바위','보'}:
#     print(item)

'''
2.for문과 딕셔너리
파이썬의 dict는 순서가 없는 비시퀸스 자료형입니다.
key 와 value 의 조합으로 데이터를 구성하기 때문에 
value만으로 데이터를 구성하는 리스트, 튜플과 같은 시퀸스 자료형과는 다른
for문 사용법을 가진다.
'''

"""
한 사람의 정보를 저장하고 있는 person 이라는 딕셔너리를 다음과 같이
생성한 person을 이용해 for문을 출력해 보자.
"""

person={
    'name':'에밀리',
    'age':20
}


for item in person:
    print(item)
#value가 아닌 'key'값이 item변수로 전달됨
#따라서 사용하려면 person[item] 으로 출력해야된다.

for key in person:
    print(person[key])
    print(person.get(key))


eng_dict ={
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주',
}
# for word in eng_dict:
#     print(f'{word}의 뜻은 {eng_dict[word]}입니다.')


'''
5개의 문자열을 입력받는데 받을 때 뜻 까지 포함해서 받고.
5개가 입력되고 나서 내가 원하는 문자열을 입력했을 때 해당 문자열의 값을 출력하세요
ex ) 1번 :문자열 입력해주세요 >>> sun
sun의 뜻을 입력해주세요 >>> 태양
2번 문자열 입력해주세요 moon 
moon의 뜻을 입력해주세요
'''

d ={

}
for i in range(1,6):
    if len(d) < 5:
        key = input(f'{i}번 문자열 입력해주세요.:')
        value = input(f'{key}의 뜻을 입력해주세요.:')
        d[key] = value
input_key = input('영어를 입력해주세요.:')
print(d[input_key])


