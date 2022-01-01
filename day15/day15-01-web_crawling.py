"""
파일 : day15-01-web_crawling
개요 : 웹 크롤링의 준비
page : 312 ~ 314
"""

'''
1. 크롬 설치하기
웹 크롤링은 웹 페이지에서 필요한 데이터를 수집하는 과정입니다.
사용자들은 인터넷 접속을 위해서 인터넷 익스플로러, 크롬, 파이어 폭스, 사파리 등
다양한 웹 브라우저를 사용함
-> 저희는 크롬을 사용할 것

* 왜 ??? Chrome ??
크롬에 있는 '개발자 도구'를 이용해서 크롤링을 수행할 때 필요한 정보를 확인하기 쉽기 때문 
'''

'''
2. robots.txt
웹 사이트에 웹 크롤러같은 로봇들의 접근을 제어하기 위한 규약
권고안이라서 지킬 의무는 없지만, 서버 주인 입장에서는 원치않은 크롤링이 들어오는데
계속해서 서비스를 제공할 의무 또한 없으므로 크롤러의 아이피를 차단하거나 임시로 막는 경우가
생깁니다.
* 서버 주인 입장에서는 크롤링이 감지되면 해당 서버의 트래픽이 올라감.
-> 트래픽 올라간다 -> 서버 주인이 지불해야할 금액이 올라간다.

robots.txt는 웹사이트의 최상위 경로(=루트)에 있어야한다.

써있는 단어들의 의미는 다음과 같다.
User-agent: 제어할 로봇의 User-Agent
Disallow : 허용하지 않을 경로 
Allow : 허용할 경로
/$ : 첫 페이지만 허가 
'''

'''
3. requests 라이브러리 설치하기
사용자는 웹을 이용할 때 서버에 여러 가지 요청을 진행합니다.
검색어를 입력한 뒤 검색 결과를 요청하기도 하고, 아이디와 비밀번호를 입력한 뒤 로그인을
요청하기도 합니다.
사용자가 서버에 요청하는 것을 request(요청)라고 합니다. 
requests 라이브러리는 쉽고 편리하게 request를 처리할 수 있는 기능을 가지고있습니다.
* 설치 방법
[ 원하는 파이썬 설치 ]
-> 원하는 파이썬 설치 경로/Scripts 이동
-> cmd ( 명령 프롬프트 )를 실행
-> pip install requests 입력 후 엔터
'''

'''
4. BeautifulSoup 패키지 설치
BeautifulSoup은 구문을 분석해서 필요한 내용만 추출할 수 있는 기능을 가지고 있는 외부
패키지입니다.
requests와 마찬가지로 외부 패키지이기 때문에 설치가 필요합니다.
* 설치 방법
[ 원하는 파이썬 설치 ]
-> 원하는 파이썬 설치 경로/Scripts 이동
-> cmd ( 명령 프롬프트 )를 실행
-> pip install BeautifulSoup4 입력 후 엔터 
'''












