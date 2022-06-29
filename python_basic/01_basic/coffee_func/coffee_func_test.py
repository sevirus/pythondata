import coffee_func as cf
import os

path = os.path.dirname(__file__)

item = {'아메리카노' : 2000,
       '라떼' : 1500,
       '캐모마일' : 2000,
       '페퍼민트' : 1300}

menu_display = '''
---------------------------------------------------------
1.커피 자판기    2.메뉴 추가    3.메뉴 삭제    4.메뉴 목록   5.종료
---------------------------------------------------------
>>>'''
while True:
    menu = input(menu_display)
    if menu == '1':
        cf.coffee_choice(item)
    elif menu == '2':
        cf.coffee_insert(item)
    elif menu == '3':
        cf.coffee_delete(item)
    elif menu == '4':
        cf.menu_list(item)
    elif menu == '5':
        print(path)
        cf.data_save(path + '/item.json', item)
        break
    else:
        print('올바른 메뉴를 선택해주십시오.')
