import math
import random

# EASY
# Задача-1:
a = ["яблоко", "банан", "киви", "арбуз"]
print(a)
for val in range(len(a)):
    print("{}. {}".format(val + 1, a[val]))

# EASY
# Задача-2:
a = [1, 3, 5, 7, 9, 11]
b = [3, 7, 11]
c = []
for val1 in a:
    if val1 not in b:
        c.append(val1)
print(c)

# EASY
# Задача-3:
a = [1, 4, 16, 27, 99, 17, 44, 51]
b = []
for val in a:
    if not val % 2:
        val = val / 4
        b.append(val)
    else:
        val = val * 2
        b.append(val)
print(b)

# NORMAL
# Задача-1:
a = [1, 4, 16, 27, 99, 17, 44, 51, 81]
b = []
for num in a:
    if num > 0:
        if math.sqrt(num).is_integer():
            b.append(math.sqrt(num))
print(b)

# NORMAL
# Задача-2:
date = input('Введите дату в формате dd.mm.yyyy: ')
days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
        '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
        '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
        '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
        '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
        '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое',
        '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
        '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}

months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
          '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
          '11': 'ноября', '12': 'декабря'}

date_list = date.split('.')
print(f"Дата: {days.get(date_list[0])} {months.get(date_list[1])} {date_list[2]} года")

# NORMAL
# Задача-3:
numbers = []
n = int(input("Введите число элементов списка: "))
for i in range(n):
    numbers.append(random.randint(-100, 100))
print(numbers)

# NORMAL
# Задача-4:
a = [1, 4, 16, 27, 99, 17, 16, 51, 4, 44, 51, 81]
b = []
c = set()
for num in a:
    if a.count(num) == 1:
        b.append(num)
    else:
        c.add(num)
print("Не повторяющиеся элементы списка a: \n", b)
print("Повторяющиеся элементы списка a: \n", c)

# HARD
# Задача-1:
a = 'y=3x+7'
x = 2.5
eq = list(a)
eq[eq.index('x')] = x
y = float(eq[2])*float(eq[3])+float(eq[5])
print(y)

# HARD
# Задача-2:
date = input('Введите дату в формате dd.mm.yyyy: ')
date_list = date.split('.')
months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
          '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
          '11': 'ноября', '12': 'декабря'}
if not len(date_list[0]) == 2 and len(date_list[1]) == 2 and len(date_list[2]) == 4:
    print("Формат даты некорректный. Дата должна быть в формате dd.mm.yyyy")
if not 1 < int(date_list[2]) < 9999:
    print("Год введен некорректно.")
if months.get(date_list[1]):
    if int(date_list[1]) % 2:
        if 1 < int(date_list[0]) < 31:
            print(f"Дата для {date_list[0]} {months.get(date_list[1])} {date_list[2]} года введена корректно.")
        else:
            print(f"Дата введена не корректно.")
    else:
        if 1 < int(date_list[0]) < 31:
            print(f"Дата для {date_list[0]} {months.get(date_list[1])} {date_list[2]} года введена корректно.")
        else:
            print(f"Дата введена не корректно.")
else:
    print("Месяц введен некорректно")
