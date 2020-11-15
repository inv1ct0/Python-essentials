# Python essentials

Algorithms:
В папке примеры реализации популярных алгоритмов

Урок 1.

EASY
Задача-1: поработайте с переменными, создайте несколько,
выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
Задача-2: Запросите от пользователя число, сохраните в переменную,
прибавьте к числу 2 и выведите результат на экран.
Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
Задача-3: Запросите у пользователя его возраст.
Если ему есть 18 лет, выведите: "Доступ разрешен",
иначе "Извините, пользование данным ресурсом только с 18 лет"

NORMAL  
Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
и сообщаете об диапазоне допустимых. И просите ввести заного.
Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
Задача-2: Исходные значения двух переменных запросить у пользователя.
Поменять значения переменных местами. Вывести новые значения на экран.
Решите задачу, используя только две переменные.
Подсказки:
* постарайтесь сделать решение через действия над числами;

HARD
Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
Формула не отражает реальной действительности и здесь используется только ради примера.
Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

Урок 2.

EASY
Задача-1:
Дан список фруктов.
Напишите программу, выводящую фрукты в виде нумерованного списка,
выровненного по правой стороне.
Пример:
Дано: ["яблоко", "банан", "киви", "арбуз"]
Вывод:
1. яблоко
2.  банан
3.   киви
4.  арбуз

Подсказка: воспользоваться методом .format()
Задача-2:
Даны два произвольные списка.
Удалите из первого списка элементы, присутствующие во втором списке.
Задача-3:
Дан произвольный список из целых чисел.
Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

NORMAL
Задача-1:
Дан список, заполненный произвольными целыми числами, получите новый список,
элементами которого будут квадратные корни элементов исходного списка,
но только если результаты извлечения корня не имеют десятичной части и
если такой корень вообще можно извлечь
Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
Склонением пренебречь (2000 года, 2010 года)
Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
в диапазоне от -100 до 100. В списке должно быть n - элементов.
Подсказка:
для получения случайного числа используйте функцию randint() модуля random
Задача-4: Дан список, заполненный произвольными целыми числами.
Получите новый список, элементами которого будут:
а) неповторяющиеся элементы исходного списка:
например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
б) элементы исходного списка, которые не имеют повторений:
например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

HARD
Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
Определить координату y точки с заданной координатой x.
Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
Проверить, корректно ли введена дата.
Условия корректности:
1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
(в зависимости от месяца, февраль не учитываем)
2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
4. Длина исходной строки для частей должна быть в соответствии с форматом
(т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
Вавилонцы решили построить удивительную башню —
расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
Она устроена следующим образом — на первом этаже одна комната,
затем идет два этажа, на каждом из которых по две комнаты,
затем идёт три этажа, на каждом из которых по три комнаты и так далее:
        ...
    12  13  14
    9   10  11
    6   7   8
      4   5
      2   3
        1

Эту башню решили оборудовать лифтом --- и вот задача:
нужно научиться по номеру комнаты определять,
на каком этаже она находится и какая она по счету слева на этом этаже.

Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.

Пример:
Вход: 13
Выход: 6 2
Вход: 11
Выход: 5 3

Урок 3.

EASY
Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!
Задание - 1 Создайте функцию, принимающую на вход Имя, возраст и город проживания человека Функция должна
возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

NORMAL  
Задание - 1
Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
Есть условие, не отображать людей получающих более зарплату 500000, как именно
выполнить условие решать вам, можете не писать в файл
можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
если скажем эти файлы потом придется передавать.
Так же при выводе имя должно быть полностью в верхнем регистре!
Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

HARD  
Задание - 1
Давайте опишем пару сущностей player и enemy через словарь,
который будет иметь ключи и значения:
name - строка полученная от пользователя,
health - 100,
damage - 50.
Поэксперементируйте с значениями урона и жизней по желанию.
Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
функция в качестве аргумента будет принимать атакующего и атакуемого,
функция должна получить параметр damage атакующего и отнять это количество
health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

Задание - 2
Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

Сохраните эти сущности, полностью, каждую в свой файл,
в качестве названия для файла использовать name, расширение .txt
Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
пока у одного из них health не станет меньше или равен 0.
После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

Урок 4. 

EASY  
Задание-1:
Дан список, заполненный произвольными целыми числами.
Получить новый список, элементы которого будут
квадратами элементов исходного списка
[1, 2, 4, 0] --> [1, 4, 16, 0]
Задание-2:
Даны два списка фруктов.
Получить список фруктов, присутствующих в обоих исходных списках.
Задание-3:
Дан список, заполненный произвольными числами.
Получить список из элементов исходного, удовлетворяющих следующим условиям:
+ Элемент кратен 3
+ Элемент положительный
+ Элемент не кратен 4

NORMAL
Эти задачи необходимо решить используя регулярные выражения!
Задача - 1
Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
Например:
Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
Задача - 2:
Вам дан текст:
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

Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
более одной точки, при любом исходе сообщите результат пользователю!

HARD  
Задание:
Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!