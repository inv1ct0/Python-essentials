# # EASY
# # Задание - 1
# print((lambda firstname, age, city: f'{firstname}, {age} год(а), проживает в городе {city}')('Алексей', 32, 'Москва'))
#
# # NORMAL
# # Задание - 1
# names = ['Alex', 'Bob', 'Mike', 'John', 'Steve', 'Jacob']
# salaries = [100000, 12100, 20000, 900000, 15000, 160000]
# result = dict(zip(names, salaries))
# with open('salary.txt', 'w') as f:
#     for key, value in result.items():
#         f.write(f'{key} - {value}\n')
#
# with open('salary.txt') as f:
#     data = f.read()
#     data_list = data.split()
#     n = []
#     s = []
#     for value in data_list:
#         if value.isnumeric():
#             s.append(value)
#         elif value.isalpha():
#             n.append(value)
#     for value in range(len(s)):
#         clean_salary = round(float(s[value]) * 0.83, 2)
#         s[value] = str(clean_salary)
#     clean_result = dict(zip(n, s))
#     for key, value in clean_result.items():
#         if float(value) < 500000:
#             print(f'{key.upper()} - {value}')
#         else:
#             print(f'{key.upper()} - ******')
#
# # HARD
# # Задание - 1
# player = {'name': input('Введите имя игрока: '), 'health': 200, 'damage': 34}
# enemy = {'name': input('Введите имя противника: '), 'health': 190, 'damage': 27}
#
#
# def attack(pl, en):
#     print('Данные игроков')
#     for key, value in pl.items():
#         print(f'{key} - {value}')
#     print('------------')
#     for key, value in en.items():
#         print(f'{key} - {value}')
#     print('------------')
#     while (en.get('health') > 0) and (pl.get('health') > 0):
#         print(f'{pl.get("name")} наносит урон {pl.get("damage")}')
#         en.update({'health': en.get('health') - pl.get('damage')})
#         print(f'{en.get("name")} наносит урон {en.get("damage")}')
#         pl.update({'health': pl.get('health') - en.get('damage')})
#     if en.get('health') <= 0 and pl.get('health') <= 0:
#         print('Ничья!\nИспытайте свои силы еще раз!')
#     elif en.get('health') <= 0:
#         print(f'Победил {pl.get("name")}')
#     else:
#         print(f'Победил {en.get("name")}')
#
#
# attack(player, enemy)

# HARD
# Задание - 2
player = {'name': input('Введите имя игрока: '), 'health': 200, 'damage': 34, 'armor': 1.2}
enemy = {'name': input('Введите имя противника: '), 'health': 190, 'damage': 27, 'armor': 2.4}


def attack(pl, en):
    print('Данные игроков')
    for key, value in pl.items():
        print(f'{key} - {value}')
    print('------------')
    for key, value in en.items():
        print(f'{key} - {value}')
    print('------------')
    while (en.get('health') > 0) and (pl.get('health') > 0):
        print(f'{pl.get("name")} наносит урон {damage_calc(pl.get("damage"), en.get("armor"))}')
        en.update({'health': en.get('health') - damage_calc(pl.get('damage'), en.get("armor"))})
        print(f'{en.get("name")} наносит урон {damage_calc(en.get("damage"), pl.get("armor"))}')
        pl.update({'health': pl.get('health') - damage_calc(en.get('damage'), pl.get("armor"))})
    if en.get('health') <= 0 and pl.get('health') <= 0:
        print('Ничья!\nИспытайте свои силы еще раз!')
    elif en.get('health') <= 0:
        print(f'Победил {pl.get("name")}')
    else:
        print(f'Победил {en.get("name")}')


def damage_calc(damage, armor):
    return damage // armor


attack(player, enemy)
