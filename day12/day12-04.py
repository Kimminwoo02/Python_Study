"""
상속

"""

'''
1. 상속?
파이썬
- 어떤 클래스가 가지고 있는 기능을 그대로 물려 받아서 사용할 수 있는 클래스를 만든다!
다른 클래스의 기능을 물려 받을 때 상속 받는다는 표현을 사용합니다!

-> 상속 관계에 있는 클래스를 표현할 때
부모 클래스 자식 클래스 용어 사용!

[관계도]
부모 클래스(상속 해주는 클래스) -> 자식 클래스( 상속받는 클래스)

용어
부모 클래스 = 슈퍼 클래스 = 기반 클래스

자식 클래스 = 서브 클래스 = 파생 클래스 

* 파이썬에서는 Super리는 키워드를 사용하여 부모클래스르 지정합니다.
부모 클래스 -> 슈퍼 클래스라 지칭
자식 클래스 -> 서브 클래스


'''

'''
2. 상속 관계 구현

[조건]
- 두 클래스가 IS-A 관계를 성립해야 합니다
    ㄴ IS -A == '~은 ~이다' 
    ex) 학생은 사람이다 => student is a person
    =student ==서브클래스
    =Person == 슈퍼클래스
    
    
사용법
- 슈퍼 클래스는일반 클래스 처럼 구현
- 서브 클래스는 어떤 클래스를 상속받고 있는지 명시를 해야한다!

[형식]
- 슈퍼클래스
class 슈퍼 클래스:
    본문
    
- 서브클래스
class 서브클래스 (슈퍼클래스):
    본문    
    
* 서브 클래스를 구현할 때 괄호 안에 어떤 슈퍼 클래스를 상속 받았는지 명시
* 상속 관계에 놓인 서브 클래스는 마치 자신의 것처럼 슈퍼 클래스의 기능을 사용 가능!



'''


# 슈퍼 클래스
class Person:

    def __init(self,name):
        self.name = name

    def eat(self,food):
        print(f'{self.name}가{food}를 먹습니다.')

# 서브 클래스
# class Student(Person):
#
#     def __init__(self,name,school):
#         super().__init(name)
#         self.school=school
#
#     def study(self):
#         print(f'{self.name}는 {self.school}에서 공부를 합니다.')
#
# potter = Student('해리포터','호그와트')
# potter.eat('감자')
# potter.study()


'''
Person 은 슈퍼 클래스 이고
name 을 전달해서 생성할 수 있으며 eat() 메소드를 가지고 있습니다

Student 는 서브클래스입니다
name과 school을 전달해서 생성할 수 있으면 study() 메소드를 가지고 있습니다.

Student는 Person 슈퍼 클래스를 상속 받았기 때문에
person() 클래스의 eat() 메소드도 사용할 수 있습니다!

* Student 클래스의 생성자가 중요!

'''

'''
3. 서브 클래스의 __init__()
- 서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없다!
-부모가 존재해야 자식도 존재할 수 있다!
-이와 같이 서브 클래스의 생성자를 구현할 때는 반드시 슈퍼 클래스의 생성자를 먼저
호출해야 합니다!
-super 키워드를 사용합니다. (슈퍼클래스를 의미합니다.)

'''

'''
4. 서브 클래스의 인스턴스 자료형
슈퍼 클래스 객체는 슈퍼 클래스의 인스턴스 입니다.
그에 비해 서브 클래스 객체는 서브 클래스의 인스턴스 이면서 
동시에 슈퍼 클래스의 인스턴스 입니다.
-> student Object == Person Object

-어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해서
isinstance() 함수를 사용합니다

[사용법]
isinstance(객체,클래스)

[반환값]
Ture or False

'''

# print(isinstance(potter,Student))
# print(isinstance(potter,Person))

'''
책 예제 원두를 저장하는 CoffeE 클래스와 원두에 물을 섞은 espresso 클래스를
상속 관계로 구현해보자

'''

class Coffee:

    def __init__(self,bean):
        self.bean = bean

    def coffee_info(self):
        print(f'원두{self.bean}')
class Espresso(Coffee):
    def __init__(self,bean,water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print(f'물{self.water}ml')
coffee =Espresso('콜롬비아',30)
coffee.espresso_info()
