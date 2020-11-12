# EASY
# Задача 1
a = 10
b = 20
c = int(input("Введите число: "))
print(a, b, c)


# EASY
# Задача 2
d = int(input("Введите число: "))
print("Сумма чисел а, b и числа введенного Вами:", d + 2)

# EASY
# Задача 3
d = int(input("Введите Ваш возраст: "))
if d >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

# NORMAL
# Задача 1
a = int(input("Введите число от 0 до 10: "))
while (a < 0) or (a > 10):
    print("Вы ошиблись")
    a = int(input("Введите число от 0 до 10: "))
else:
    print(a**2)

# NORMAL
# Задача 2
a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))

a = a + b
b = b - a
b = -b
a = a - b
# a, b = b, a
print("a = ", a, "\nb = ", b)

# HARD
# Задача 1
name = input("Введите имя пациента: ")
surname = input("Введите фамилию пациента: ")
age = int(input("Введите возраст пациента: "))
weight = int(input("Введите вес пациента: "))
if (age < 30) and (50 < weight < 120):
    print(name, surname, ", возраст", age, "лет, вес", weight, "кг : Хорошее состояние")
elif (age > 30) and ((weight < 50) or (weight > 120)):
    print(name, surname, ", возраст", age, "лет, вес", weight, "кг : Следует заняться собой")
elif (age > 40) and ((weight < 50) or (weight > 120)):
    print(name, surname, ", возраст", age, "лет, вес", weight, "кг : Следует обратится к врачу!")
else:
    print(name, surname, ", возраст", age, "лет, вес", weight, "кг : Консультация не требуется")
