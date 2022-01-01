"""
웹 크롤링

"""

'''
1. 크롬 준비
구글 검색창에 크롬 다운로드 -> 크롬 설치

'''

'''
2. requests 모듈 설치
python 설치 디렉토리 -> Scripts -> cmd -> pip.exe install requests

'''

'''
3. BeatifulSoup 모듈 설치
Python 설치 디렉토리 -> Scripts -> cmd -> pip.exe install BeautifulSoup4

'''
'''
import requests
re = requests.get('https://www.naver.com')

print(re.text)

'''