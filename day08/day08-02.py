"""
사용자 함수 용어

"""

'''
함수 용어 정리
용어에 대해서 알 필요가 있다.
1. 함수 정의 : 사용자 함수를 새로 만드는 것을 의미
2. 인수 : 사용자 함수에 전달할 입력(input)을 의미!
 -> argument 라고도 한다!
3. 매개변수 : 인수를 받아서 자장하는 변수를 의미. parameter라고도 합니다. 
4. 반환값: 사용자 함수의 출력을 의미합니다. return 이라고도 한다
5. 함수 호출 : 만들어진 사용자 함수를 실제로 사용하는 것을 의미한다!
'''

'''
1.함수 정의
사용자 함수를 정의하려면 def 키워드를 사용합니다.
P에서 사용자 함수를 정의하는 방법은 다음과 같다.

def 함수이름 (매개변수):
    본문
    return 반환값
    
* 여기서 함수 이름은 개발자가 마음대로 결정할 수 있다.
- > 함수 이름은 정할 때 그 함수가 어떤 동작을 하는지 나타나면 좋다!
함수 이름 오른쪽에 괄호 안의 매개변수는 함수에 전달되는 
인수(입력)이 저장될 변수입니다.

함수에 전달되는 인수가 없으면 작성하지 않아도 된다!.
    
함수에 전달되는 인수가 없으면 작성하지 않아도 된다.

중요
함수의 본문은 모두 들여쓰기 문법을 적용합니다!!!!!!!
if, for문 처럼 들여쓰기를 해야합니다.

return 부분은 함수의 반환값(출력)이 있는 경우에는 반드시 작성하고,
반환값이 없으면 작성하지 않아도 된다!   
'''

'''
2. 함수호출 
'함수를 호출한다? '는 정의된 함수를 사용하겠다는 소리입니다.
사용자 함수를 호출하는 방법은 다음과 같습니다.
-기본적인 함수 허츨 방법.
변수 = 함수 이름(인수)
'''

# number = input("번호를 입력해주세요>>>:") #인풋 괄호 안의 부분이 인수이다!
# 변수 =  함수 ( 인수 )
'''
함수 호출은 인수(입력) 과 반환값(출력) 의 유무에 따라 달라집니다.
만약 함수에 전달할 인수(입력)이 없다면 인수를 생략할 수 있습니다.
반환값(출력)이 없다면 함수의 호출 결과를 저장할 변수를 생략할 수 있습니다.!
-- 4가지 형태로 함수를 호출 할 수 있다.
'''
# 1) 인수 x, 반환값 x
# 함수이름()

# 2) 인수 o , 반환값 x
# 함수 이름(인수)
print('안녕하세요')

#3) 인수 x, 반환값 o
# 변수 = 함수 이름()

# 4) 인수 o, 반환값 o
# 변수 = 함수 이름 (인수)
rg = range(1)

'''
반환값이 없는 경우 1)번과 2)번 호출 형태만 기억하면 된다!
** 반환값이 있는 경우?
사실 반환 값이 있는 경우 위에서 소개한 호출 형태보다 더 많은 호출 형태가 
있을 수 있다.

반환 값은 출력 결과를 의미하기 때문에 출력 결과를 처리할 수 있는 형태라면 
어떤 형태든지 가능합니다.

다음 호출형태를 보고 반환값이 있는지 없는지 판단해보자!

print(함수 이름())
함수 이름(함수이름()) 이런식으로 할 때도 있다.
--정답은 반환값이 있다!
함수 호출의 결과인 반환값이 print() 함수의 인수로 전달되면서 
반환값이 출력되는 형태이다!

이처럼 반환값이 있다고 해서 반드시 반환 값을 저장할 변수가 있어야하는것은 아닙니다.
'''

#welcome 함수 정의
#- 함수 실행하면 다음과 같은 출력을 해준다.
# hello Python
# Nice to meet you

def welcome():
    print("hello Python ")
    print("Nice to meet you")

welcome()


'''
welcome 함수는 인수입력이 없어 welcome 뒤의 괄호 안에 작성하는 매개변수가 없고 반환값도 없어 
함수 내부에 리턴문도 존재하지 않는다!

** 모든 사용자 함수는 '항상' 함수 정의가 끝난 뒤에 함수를 호출해야합니다.
(함수가 호출보다 뒤로 갈 수 없다)

'''

def welcome2():
    print("안녕하세요")

'''
예제 다음과 같은 함수를 만들어보자!
함수명 : welcome
실행 출력
안녕하세요
반갑습니다.
어서오세요.
'''

def welcom():
    print("안녕하세요.")
    print("반갑습니다.")
    print("어서오세요")
welcom()

'''
다음을 만들어 보자
함수명 welcom2
0안녕하세요
.
.
.
6안녕하세요
'''
def welcom2():
    for i in range(7):
        print(f"{i}안녕하세요")

welcom2()

'''
다음 코드를 줄여보세요!
print('python hi!')
!느낌표가 5번까지 돈다.
'''

def welcome2():
    a = '!'
    for i in range(6):
        a +=  i
        print(f'안녕하세요{a}')