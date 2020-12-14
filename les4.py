import random
import re

# EASY
# Задание-1:
a = [random.randint(0, 100) for _ in range(10)]
b = [val * 2 for val in a]
print(b)

# Задание-2:
fruits_1 = ['apple', 'banana', 'pineapple', 'orange', 'lemon']
fruits_2 = ['banana', 'strawberry', 'orange']
fruits = list(filter(lambda el: el in fruits_1, fruits_2))
print(fruits)

# Задание-3:
c = [random.randint(-50, 50) for _ in range(10)]
d = [val for val in c if (val % 3 == 0) and not (val % 4 == 0) and (val > 0)]
print(d)

# NORMAL
# Эти задачи необходимо решить используя регулярные выражения!
# Задача - 1
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
email = input('Введите email: ')
pattern_email = '[a-z0-9_]+@[a-z]+\.(ru|org|com)'
pattern_name = '^[A-Z][a-z]*'
print(re.match(pattern_name, name))
print(re.match(pattern_name, surname))
print(re.match(pattern_email, email))

# Задача - 2:
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern_dot = '\.{2,}'
print(re.search(pattern_dot, some_str))
