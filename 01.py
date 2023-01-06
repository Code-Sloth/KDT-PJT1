'''
아래의 내용을 01.txt에 기록하세요.
Hello, Python!
1일차 파이썬 공부 중
2일차 파이썬 공부 중
3일차 파이썬 공부 중
4일차 파이썬 공부 중
5일차 파이썬 공부 중
'''

with open('01.txt', 'w', encoding = 'UTF8') as f:
    f.write('Hello, Python!\n')
    for i in range(1,6):
        f.write(f'{str(i)}일차 파이썬 공부 중\n')
        