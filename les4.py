import random

# EASY
# Задание-1:
a = [random.randint(0, 100) for _ in range(10)]
b = [val*2 for val in a]
print(b)

# Задание-2:
fruits_1 = ['apple', 'banana', 'pineapple', 'orange', 'lemon']
fruits_2 = ['banana', 'strawberry', 'orange']
fruits = list(filter(lambda el:el in fruits_1, fruits_2))
print(fruits)

# Задание-3:
c = [random.randint(-50, 50) for _ in range(10)]
d = [val for val in c if (val % 3 == 0) and not (val % 4 == 0) and (val > 0)]
print(d)
