"""

CSV 파일 입출력

"""
import csv

'''

1.CSV?
CSV = comma separated Values 의 약자 즉 분리된 값
-> 쉼표로 분리한 값들!
-> 데이터 베이스나 스프레드 시트 데이터를 저장하기 위해서 사용하는 형식!
-> 엑셀 같은 스프레드시트에서는 쉼표가 아닌 각 데이터가 분리되어있는 것 처럼 보임!
 ( 메모장으로 CSV 파일을 열어보면 ',' 쉼표로 데이터가 구분되어 있는게 보임!)
'''

'''
2.CSV 모듈로 CSV 파일 생성하기!
csv 모듈을 이용해보자!

사용법
-1. csv 파일을 w모드로 열기
-2. 열린 file을 csv.writer() 메소드 인수에 전달
-3. writerow 메소드를 이용해 값을 전달.
-4. newline 옵션을 이용해서 불필요한 라인 제거!

'''
# file = open('차량관리.csv','w',newline='')
with open('차량관리.csv','w',newline='') as file:
    csv_maker = csv.writer(file,delimiter=',',quotechar='"')
    csv_maker.writer([1, '08러1234','2020-10-20,14:00'])
    csv_maker.writer([2, '25러1234', '2020-10-20,14:10'])
    csv_maker.writer([3, '28러1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다!')
