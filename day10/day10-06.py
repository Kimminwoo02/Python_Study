"""

퀴즈!

"""

'''
1.나라별 수도를 순차적을 반복시켜서 nation 리스트에 저장해 두었습니다!
nation 리스트의 내용을 이용하여 다음과 같은 nation.txt 파일을 생성하세요!

[변수]
nation = ['그리스','아테네','독일','베를린','러시아','모스크바','미국','워싱턴']

[출력(파일 내부)]
그리스 - 아테네
독일 - 베를린
러시아 - 모스크바
미국 - 워싱턴

[조건]
with,(file,close)
'''

nation = ['그리스','아테네','독일','베를린','러시아','모스크바','미국','워싱턴']
with open('nation.txt','wt') as file:
    # file.write(f'{nation[0]}-{nation[1]}')
    # file.write(f'{nation[2]}-{nation[3]}')
    # file.write(f'{nation[4]}-{nation[5]}')
    # file.write(f'{nation[6]}-{nation[7]}')

#위에는 하드코딩이라 불리운다!( 멍청한 방법)
    for i in range(0,8,2):
        file.write(f'{nation[i]}-{nation[i+1]}\n')


'''
2. 웹하드에 업로드되어 있는 '연락처.txt' 파일을 사용합니다.
연락처.txt 파일에 저장된 연락처 중에서 전화번호가 011로 시작하는 모든 연락처를 010으로 시작하도록 파일을
수정하세요!
[지시사항]
연락처.txt파일은 다음과 같은 형식으로 데이터가 저장되어 있습니다!
"김나라","목포시","010-1111-1111"
"이나라","목포시","011-1111-1111"
"저나라","목포시","011-1111-1111"
"잠나라","목포시","010-1111-1111"

[출력 콘솔]
총 3건의 011 데이터를 찾았습니다.
모든 데이터를 수정했습니다!
'''

with open('연락처.txt','wt') as file:
    file.write('"김나라","목표시","010-1111-1111"\n')
    file.write('"이나라","목표시","011-1111-1111"\n')
    file.write('"저나라","목표시","011-1111-1111"\n')
    file.write('"잠나라","목표시","010-1111-1111"\n')
    file.write('"오나라","목표시","010-1111-1111"\n')

file = open('연락처.txt','rt')
line_list =file.readlines()
total = 0
for index,line in enumerate(line_list):
    splits = line.split(',')
    if splits[2].find('011') > -1:
        total += 1
        line_list[index] = line.replace('011','010')
print(f'총{total}건의 011 데이터를 찾았습니다.')
file.close()
with open('연락처.txt','wt') as file:
    for line in line_list:
        file.write(line)
print('모든 데이터를 수정했습니다.')

'''
at, wt
wt : 덮어쓰기
at : 추가
'''