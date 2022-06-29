# 타자게임
# 데이터 저장 : word = []
# word 리스트에서 문제를 추출하여 제출하면 맞추는 게임
# -한번 출제된 문제는 맞출 때까지 반복
# - 전체 5문제를 출제 다 맞추면 종료

import json, time, os, random
word = []
path = os.path.dirname(__file__) # __file__ 파일에 대한 정보. 어느 경로에 있는지 찾아줌
print(path)
f = open(path + '/word.json', 'r')
word = json.load(f)
f.close()

rank = {'aaa': 11.2151312, 'bbb': 17.1231532}

menu_display = '''
---------------------------------------------------------
1.게임 시작     2.문제 추가    3.문제 저장    4.등수 리스트   5.종료
---------------------------------------------------------
>>>'''

while True:
    menu = input(menu_display)
    if menu == '1':
        print('게임 시작!')
        start = time.time()
        n = 1
        quiz = random.choice(word)
        while n <= 5:
            print(f'{n}번')
            print(quiz)
            result = input('>>>')
            if quiz == result:
                print('통과')
                n += 1
                quiz = random.choice(word)
            else:
                print('틀렸습니다!')
        print('5문제 완료!')
        end = time.time()
        print(f'걸린 시간은 {end-start:.0f}초')
        name = input('이름을 입력하세요 >>>')
        rank[name] = end-start
        print(rank)
    elif menu == '2':
        print('문제 추가 작업!')
        while True:
            data = input('(종료:Enter)>>>')
            if data == '':
                break
            word.append(data)
            print(word)
    elif menu == '3':
        print('문제 저장 작업!')
    elif menu == '4':
        print('등수 리스트')
        for index, (k, v) in enumerate(sorted(rank.items(), key=lambda x : x[1])):
            print(f'{index+1}등 {k} 시간: {v:.0f}')
    elif menu == '5':
        print('종료!')
        f = open(path + '/word.json', 'w')
        json.dump(word, f)
        f.close()
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')