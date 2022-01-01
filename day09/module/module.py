"""

컨버터 모듈을 import 시켜 해당 모듈에 있는 함수 사용!
*** import
모듈안에 컨버터랑 모듈이 같은 폴더에 있어야 된다!
"""
import converter

#모듈 우측 클릭 -> mark directory as ->


#1.str - int
print(converter.str_to_int('1','2','3','4'))

#2. int-> str
print(converter.int_to_str(1,2,3,4))
#3 float -> str
print(converter.float_to_str(1.0,1.2,1.5,1.7,2.0))
#4. str->float
print(converter.str_to_float('1.0','1.2','1.5','1.7','2.0'))

# 컨버터를 앞에 써주는게 너무 귀찮다...
#print(set(converter.int_to_str(1,2,3,4)))
#->