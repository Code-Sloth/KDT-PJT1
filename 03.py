'''
과일 데이터 fruits.txt를 활용하여 이름이 berry로 끝나는 과일의 개수와 목록을 03.txt 에 기록하세요.

과일은 한 줄 당 1개만 기록되어 있습니다.
'''

with open('data/fruits.txt', 'r', encoding = 'UTF8') as f:
    berry = []
    data = f.readlines()
    for i in data:
        if i.endswith('berry\n'):
            if i not in berry:
                berry.append(i)
            
with open('03.txt', 'w', encoding = 'UTF8') as f2:
    f2.write(f'{str(len(berry))}\n')
    f2.writelines(berry)

    