"""
import를 사용해서 모듈을 가져올 때! 별명을 사용해보자!

"""

import converter as cvt
""" converter 모듈을 사용할건데 
이 모듈명을을 cvt로 별명을 지어주고 쓴다
converter=cvt
"""

print(cvt.int_to_str(1,2,3,4,5,6))

#from 모듈 import 도 별명을 지어줄 수 있다!
from converter import int_to_str as its
print(its(1,2,3,4,5,6))

# as 를 이용해서 별명을 짓는건 많이 사용된다!
# 알아둬야 선임이 쓸 떄 파악하기 쉽다!

'''

2.모듈의 생성
-module/converter.py 만들엇다
'''


'''
3.모듈의 사용
import를 해야 해당 모듈을 사용할 수 있다.
import를 사용하는 방법은 2가지가 있다.

3-1 import : '모듈 전체'를 가져오는 방법
            -> 모듈에 저장된 모든 '클래스'나 함수를 사용하고자 할 때 사용된다.
            -> 가장 쉽게 모듈을 가져올 수 있는 방법
[형식]
import 모듈

3-2. from 모듈 import 함수 : '모듈에 포함된 함수' 중에서 특정 함수만 골라서 
                            가져오는 방법
[형식]            
from 모듈 import 함수
        - 모듈에서 함수 하나만 가져오는 방식
from 모듈 import *
        - 모듈에서 모든 함수를 가져오는 방식
from 모듈 import 함수1, 함수2
        - 모듈에서 함수 두 가지를 가져오는 방식

'''

'''
4. 별명 사용하기
모듈이나 함수 import하는 경우 원래 이름 대신 별명(alias) 사용합니다.
* 모듈이나 함수의 이름이 긴 경우 주로 짧은 별명을 지정하고
    긴 본래 이름 대신 사용.

[형식]
4-1 import
    import 모듈 as 별명

4-2 from import
    from 모듈 import 함수 as 별명
'''