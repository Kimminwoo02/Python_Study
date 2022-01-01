"""
내장함수 시퀸스

"""

'''
1.enumerate 중요!!
enumerate() 함수를 리스트와 함께 사용할 수 있습니다.
이 함수를 사용하면 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 형태로
추출됩니다.

리스트와 enumerate() 함수를 함께 사용하는 방식은 다음과 같다!

for item in enumerate(리스트):
    반복실행문
'''

for item in enumerate(['가위','바위','보']):
    print(item)

# 언패킹 **
for i, v in enumerate(['가위','바위','보']):
    print(f'index == {i}// value ={v}')
'''
2. range() 함수
range() 함수는 전달된 인수 값에 따라시퀸스 자료형의 데이터를 생성하는 함수입니다.
'특정 범위를 생성하기때문에 *생성자 라고도 한다!

주로 사용 되는곳은 for 문! 원하는 횟수만큼 for문 내부의 실행문을 실행
range() 함수의 결과 자료형은 range 이기 때문에 list나 튜플 함수를 통해서
변환해서 사용한다!

range 사용법은 다음과 같습니다!
1.range(stop)
2.range(start,stop)
3.range(start,stop,step)
'''

'''
4. len(함수)
len() 함수에 '전달된 객체'의 길이를 반환하는 함수!
'''


'''

'''