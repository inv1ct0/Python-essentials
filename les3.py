# EASY
# Задание - 1
print((lambda firstname, age, city: f'{firstname}, {age} год(а), проживает в городе {city}')('Алексей', 32, 'Москва'))

# NORMAL
# Задание - 1
names = ['Alex', 'Bob', 'Mike', 'John', 'Steve', 'Jacob']
salaries = [100000, 12100, 20000, 900000, 15000, 160000]
result = dict(zip(names, salaries))
with open('salary.txt', 'w') as f:
    for key, value in result.items():
        f.write(f'{key} - {value}\n')

with open('salary.txt') as f:
    data = f.read()
    data_list = data.split()
    n = []
    s = []
    for value in data_list:
        if value.isnumeric():
            s.append(value)
        elif value.isalpha():
            n.append(value)
    for value in range(len(s)):
        clean_salary = round(float(s[value]) * 0.83, 2)
        s[value] = str(clean_salary)
    clean_result = dict(zip(n, s))
    for key, value in clean_result.items():
        if float(value) < 500000:
            print(f'{key.upper()} - {value}')
        else:
            print(f'{key.upper()} - ******')

# HARD
# Задание - 1
player = {'name': input('Введите имя игрока: '), 'health': 200, 'damage': 34}
enemy = {'name': input('Введите имя противника: '), 'health': 190, 'damage': 27}


def attack(pl, en):
    print('Данные игроков')
    for key, value in pl.items():
        print(f'{key} - {value}')
    print('------------')
    for key, value in en.items():
        print(f'{key} - {value}')
    print('------------')
    while (en.get('health') > 0) and (pl.get('health') > 0):
        print(f'{pl.get("name")} наносит урон {pl.get("damage")}')
        en.update({'health': en.get('health') - pl.get('damage')})
        print(f'{en.get("name")} наносит урон {en.get("damage")}')
        pl.update({'health': pl.get('health') - en.get('damage')})
    if en.get('health') <= 0 and pl.get('health') <= 0:
        print('Ничья!\nИспытайте свои силы еще раз!')
    elif en.get('health') <= 0:
        print(f'Победил {pl.get("name")}')
    else:
        print(f'Победил {en.get("name")}')


attack(player, enemy)

# HARD
# Задание - 2
# player = {'name': input('Введите имя игрока: '), 'health': 200, 'damage': 34, 'armor': 1.2}
# enemy = {'name': input('Введите имя противника: '), 'health': 190, 'damage': 27, 'armor': 2.4}


def init_fight():
    player = load_player(input('Введите имя игрока для импорта настроек боя: '))
    enemy = load_player(input('Введите имя противника для импорта настроек боя: '))
    attack(player, enemy)


def attack(pl, en):
    print('Данные игроков')
    for key, value in pl.items():
        print(f'{key} - {value}')
    print('------------')
    for key, value in en.items():
        print(f'{key} - {value}')
    print('------------')
    while (int(en.get('health')) > 0) and (int(pl.get('health')) > 0):
        print(f'{pl.get("name")} наносит урон {damage_calc(int(pl.get("damage")), float(en.get("armor")))}')
        en.update({'health': int(en.get('health')) - damage_calc(int(pl.get("damage")), float(en.get("armor")))})
        print(f'{en.get("name")} наносит урон {damage_calc(int(en.get("damage")), float(pl.get("armor")))}')
        pl.update({'health': int(pl.get('health')) - damage_calc(int(en.get("damage")), float(pl.get("armor")))})
    if en.get('health') <= 0 and pl.get('health') <= 0:
        print('Ничья!\nИспытайте свои силы еще раз!')
    elif en.get('health') <= 0:
        print(f'Победил {pl.get("name")}, здоровья осталось {pl.get("health")}')
    else:
        print(f'Победил {en.get("name")}, здоровья осталось {en.get("health")}')


def damage_calc(damage, armor):
    return damage // armor


# with open(f'{player.get("name")}.txt', 'w') as f:
#     for k, v in player.items():
#         f.write(f'{k} - {v}\n')
#
# with open(f'{enemy.get("name")}.txt', 'w') as f:
#     for k, v in enemy.items():
#         f.write(f'{k} - {v}\n')

def load_player(player_name):
    with open(f'{player_name}.txt') as f:
        data = f.read()
        data_list = list(data.split())
        key = []
        val = []
        for v in range(2, len(data_list), 3):
            val.append(data_list[v])
        for k in range(0, len(data_list), 3):
            key.append(data_list[k])
        player = dict(zip(key, val))
    return player


def load_enemy(enemy_name):
    with open(f'{enemy_name}.txt') as f:
        data = f.read()
        data_list = list(data.split())
        key = []
        val = []
        for v in range(2, len(data_list), 3):
            val.append(data_list[v])
        for k in range(0, len(data_list), 3):
            key.append(data_list[k])
        enemy = dict(zip(key, val))
    return enemy


# default player's name - Bob, enemy's name  Mike
init_fight()
