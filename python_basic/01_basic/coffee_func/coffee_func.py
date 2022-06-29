import json

def coffee_choice(item):
    print('메뉴를 선택하세요')
    choice = '메뉴'
    while choice:
        for k, v in item.items():
            print(f'{k} : {v:,}원', end = ' ')
        print()
        choice = input('메뉴 선택(종료:Enter) >>> ')
        if choice == '':
            break
        money = int(input('금액 투입 >>> '))
        if choice in item.keys():
            if money >= item[choice]:
                money -= item[choice]
                print(f'{choice} 서비스 합니다. 거스름돈은 {money} 입니다.')
            else:
                print(f'투입 금액이 부족합니다. 현재 투입 금액은 {money} 입니다.')
        else:
            print('해당 메뉴가 없습니다.')


def coffee_insert(item):
    print('메뉴 추가')
    menu_name = input('메뉴명 >>> ')
    menu_price = ''
    while not menu_price.isdigit():
        menu_price = input('메뉴 가격 >>> ')
    menu_price = int(menu_price)
    
    if menu_name in item.keys():
        print(f'{menu_name} 메뉴가 있습니다. 수정합니다.')
    else:
        print(f'{menu_name} 메뉴를 추가합니다.')
    item[menu_name] = menu_price
    print(item)

def coffee_delete(item):
    print('메뉴 삭제')
    menu_name = input('삭제하려는 메뉴명 >>> ')
    if menu_name in item.keys():
        print(f'{menu_name} 메뉴가 있습니다. 삭제합니다.')
        del item[menu_name]
    else:
        print('해당 메뉴가 없습니다.')


def menu_list(item):
    print('메뉴 목록')
    menu_1 = input('1.메뉴 이름순 2.메뉴 가격순 >>> ')
    if menu_1 == '1':
        for k, v in sorted(item.items(), key=lambda x : x[0]):
            print(f'{k:25} : {v:10,}원')
    elif menu_1 == '2':
        for k, v in sorted(item.items(), key=lambda x : x[1]):
            print(f'{k:25} : {v:10,}원')

def data_load(path):
    f = open(path, 'r')
    data = json.load(f)
    f.close()
    return data

def data_save(path, data):
    f = open(path, 'w')
    json.dump(data, f)
    f.close()