"""
로컬 글로벌 변수
지역변수와 전역변수

"""

'''
1. 지역변수
함수 내부에서 선언한 변수는 함수 내부에서만 사용할 수 있는 지역변수(local variable)가 됩니다.
함수 외부에서는 지역변수에 접근할 수 없습니다!

'''

def f ():
    a = 10
    print(f'f() 내부:{a}')

f()
#print(f'f() 외부:{a}' ) # a 는 함수 내부에서만 사용할 수 있는 지역 변수이다!

'''
함수 외부에서 선언한 변수는 함수 내부나 함수 외부에서 모두 사용할 수 있습니다.
이런 변수를 전역변수 라고합니다.
'''

b= 20
def f ():
    print(f'f() 내부 {b}')

f()
print(f'f() 외부{b}')

'''
전역변수를 함수 내부에서 사용하는 경우는 2가지로 분리해서 생각해야한다.

하나는 단순한 참고!용인 경우
    ㄴ 별다른 설정 xxx
다른 하나는 전역 변수의 값을 변경하는 경우!
    ㄴ global 키워드를 통해서 전역변수의 값을 수정할 수 있도록
        전역변수 선언을 해야한다.
'''

# 전역변수를 단순히 참조!
a= 0
def f():
    a = 10
    print(a)
f()
print(a)

a = 0
def f():
    a = 10
    global a # 나는 전역변수 a를 사용할꺼야!
    print(a)
f()
print(a)

'''
global a를 빼고 a를 사용하면?
a 값은 전역 변수 a 가 아닌 지역변수 a가 생성된다!
따라서 함수 내부에서 전역변수를 사용하고 싶다면 반드시!
global 키워드가 필요합니다.

'''