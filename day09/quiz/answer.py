"""


"""

'''
개인정보의 보안처리를 위해 주어진 인수의 일부를 *로 바꿔서 
반환하는 함수를 만들어서 이를 모듈러에 저장하는 프로그램입니다.

다음과 같은 조건으로 모듈을 만들어서 사용해보세요
[모듈 생성하기]
my_secure.py
-함수
secure_name()함수: 김철수 -> 김 **
secure_no 함수 951012-1234567 -> 뒷자리 *로
secure_phone 함수: 010-1234-5677->010-****-5677

[모둘 사용하기]
현재 answer 파일에서 my_secure 모듈을 사용해서
다음과 같은 출력을 해보자!

[출력 결과]
김**
951012-******
010-****-4574
'''

import my_secure
print(my_secure.secure_name('김철수'))
print(my_secure.secure_no('950701-1234556'))
print(my_secure.secure_phone('010-5018-2344'))