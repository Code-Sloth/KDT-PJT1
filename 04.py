'''
과일 데이터 fruits.txt를 활용하여 각 과일의 이름과 등장 횟수를 04.txt 에 기록하세요.

과일은 한 줄 당 1개만 기록되어 있습니다.
'''

with open('data/fruits.txt', 'r', encoding = 'UTF8') as f:
    data2 = []
    data = f.readlines()
    for i in data:
        if i not in data2:
            data2.append(i.rstrip()+' '+str(data.count(i)))
            data2.append('\n')

with open('04.txt', 'w', encoding = 'UTF8') as f2:
    f2.writelines(data2)