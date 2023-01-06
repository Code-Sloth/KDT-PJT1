'''
과일 데이터 fruits.txt를 활용하여 작성된 총 과일 개수를 02.txt 에 기록하세요.

과일은 한 줄 당 1개만 기록되어 있습니다.
'''

with open('data/fruits.txt', 'r', encoding = 'UTF8') as f:
    data = f.readlines()
    print(len(data))

with open('02.txt', 'w', encoding = 'UTF8') as f2:
    f2.write(str(len(data)))
    