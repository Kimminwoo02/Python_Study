"""
생성자, 소멸자

"""

'''
1. 생성자

생성자 사용 이전
- 인스턴스 변수를 인스턴스 메소드를 통해서 생성하고 있었다!
* 값을 저장하는 인스턴스 메소드를 나중에 호출하기 때문에.
문제가 발생할 수 있다.

[생성자 사용 후]
해당 클래스가 객체로 생성될 때 미리 인스턴스 변수를 만들어 주어야 한다
->> 생성자가 해주는 작업

* 생성자는 객체를 생성할 때 자동으로 호출되는 메소드
-> 이미 python 에서 만들어 졌다.

'''

class A:
    pass

print(dir(A))

'''
*__ (언더바) 두개가 들어가 있는 메소드들은 파이썬에서 미리 기능과역할이 부여된 메소드이다.

[ 생성자 구조 ] 
def __init__(self, 매개변수):
    인스턴스 변수 선언


'''
#
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
# satang = Candy()
# satang.set_info('circle','brown')
# 지금 까지 사용 방법

class Candy:
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color

satang = Candy('circle','brown')

# 간결하다.

# def __init__(self,name,age)
#   self.name = name
#   self.age = age
'''
2. 소멸자
인스턴스가 생성될 때 => 생성자 호출
인스턴스가 소멸될 때 => 소멸자 호출.

[소멸자 구조]
def __del__(self):
    인스턴스 소멸시 동작할 코드
'''

class Sample:
    def __del__(self):
        print('인스턴스가 소멸됩니다,')

sample = Sample()
del sample

# 소멸자는 잘 사용을 안합니다! 생성자는 잘 사용하니까 잘 숙지!

# 책 예제2
'''
다음은 생성자와 소멸자를 이용해서 
서비스 안내 메세지를 출력하는 프로그램입니다.

[지시 사항]
-service 클래스를 만드세요!
-생성될 때 어떤 서비스를 위한 클래스인지 전달하고 해당 서비스에 대한 출력을 띄우세요!
-Service 클래스가 제거되면 해당 서비스가 종료되었다고 출력해주세요!

'''

# class Service:
#     def __init__(self,service):
#         self.service = service
#         print(f'{self.service} Service가 시작되었습니다!')
#
#     def __del__(self):
#         print(f'{self.service} Service가 소멸되었습니다.')
#
# s = Service('길 안내')
# del s

