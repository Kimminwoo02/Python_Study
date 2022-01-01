"""
메소드 : 세트 잘 사용은 안한다

"""

'''
1. 교집합
두 집합에서 공통적인 요소만 추출하여 새로운 집합을 생성하는 집합 연산입니다!
교집합은 & 또는 intersection() 메소드를 사용!

'''

s1 ={'apple','banana','cherry'}
s2 = {'apple','banana','orange'}
print(s1 & s2 )

print(s1.intersection(s2)) # 위에랑 똑같다.

'''
2. 합집합
두 집합의 모든 요소를 합친 새로운 집합을 생성하는 연산입니다!
합집합은 | 또는 union 을 사용합니다!

'''

s1={'apple','banana','cherry'}
s2={'apple','banana','orange'}
print(s1 | s2)
print(s1.union(s2))

'''
차집합
한 집합에서 다른 집합 요소를 뺀 새로운 집합을 생성하는 집합연산!
차집합은 - 연산 또는 difference() 메소드를 사용!

'''

s1 ={'apple','banana','cherry'}
s2 = {'apple','banana','orange'}
print(s1 - s2)
print(s1.difference(s2))