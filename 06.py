'''
영화 데이터 리스트 movies.json 를 활용하여 필요한 정보로만 구성된 리스트를 출력하세요.

코드 작성 전 movies.json 의 데이터 구조를 파악하세요.
movies.json 파일에서 읽은 데이터는 변수 movies_list 에 저장됩니다.
영화 데이터 리스트는 20개의 영화 데이터 요소를 저장하고 있습니다.
20개의 영화 데이터 리스트의 개별 영화 요소는 아래 조건을 만족해야합니다.
개별 영화 데이터는 아래 정보를 가진 딕셔너리입니다.
id
title
poster_path
vote_average
overview
genre_ids
'''

import json
from pprint import pprint
# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성

li = []
data = []

for j in range(6):
    data.append(input())


for k in movies_list:
    di = {} 
    for i in data:
        di[i] = k[i]
    li.append(di)
        
pprint(li)
