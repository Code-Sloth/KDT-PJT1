'''
영화 데이터 movie.json 와 장르 데이터 genres.json 을 활용하여 영화의 장르 정보를 출력하세요.

코드 작성 전 movie.json 와 genres.json 의 데이터 구조를 파악하세요.
movie.json 파일에서 읽은 데이터는 변수 movie 에 저장됩니다.
genres.json 파일에서 읽은 데이터는 변수 genres_list 에 저장됩니다.
영화 정보의 genre_ids에 있는 장르 id를 활용하여 해당 장르의 이름으로 구성된 리스트를 출력하세요.
'''

import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 
ids = movie['genre_ids']
li = []

for num in ids:
    for genre in genres_list:
        for key, value in genre.items():
            if num == value:
                li.append(genre['name'])

print(li)