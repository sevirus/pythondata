# 타자게임
# 데이터 저장 : word = []
# word 리스트에서 문제를 추출하여 제출하면 맞추는 게임
# -한번 출제된 문제는 맞출 때까지 반복
# - 전체 5문제를 출제 다 맞추면 종료

import typing_game_func as tgf
import os

path = os.path.dirname(__file__)
word = tgf.data_load(path + '/word.json')
rank = tgf.data_load(path + '/rank.json')

rank = {'aaa': 11.2151312, 'bbb': 17.1231532}

menu_display = '''
---------------------------------------------------------
1.게임 시작     2.문제 추가    3.문제 저장    4.등수 리스트   5.종료
---------------------------------------------------------
>>>'''

while True:
    menu = input(menu_display)
    if menu == '1':
        tgf.game(word, rank)
    elif menu == '2':
        tgf.quiz_add(word)
    elif menu == '3':
        print('문제 저장 작업!')
    elif menu == '4':
        tgf.rank_list(rank)
    elif menu == '5':
        tgf.game_exit(path, word)
        tgf.data_save(path + '/word.json', word)
        tgf.data_save(path + '/rank.json', rank)
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')