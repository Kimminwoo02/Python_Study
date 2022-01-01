"""
응용문제

"""

'''
3. 지시사항에 따라 노래 제목과 장르 정보를 저장할 수 있는 
Song 클래스와 가수 이름과 대표곡 정보를 저장할 수 있는 singer 클래스를 구현하세여!

'''

class Song:
    def set_song(self,title,genre):
        self.title = title
        self.genre = genre

class Singer:
    def set_singer(self,singer):
        self.singer = singer

    def hit_song(self,song):
        self.song = song

    def print_singer(self):
        print(f'가수이름 : {self.singer}')
        print(f'노래제목 : {self.song.title}({self.song.genre}')

# song 인스턴스 생성
song = Song()
song.set_song('취중진담','발라드')


# singer 인스턴스 생성
singer = Singer()
singer.set_singer('김동률')

# singer 의 대표곡 지정
singer.hit_song(song)

# singer 정보 출력
singer.print_singer()