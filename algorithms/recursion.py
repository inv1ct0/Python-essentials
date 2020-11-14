# Возведение числа в степень

def power_number(num, power):
    if power == 0:
        return 1
    elif power == 1:
        return num
    else:
        return num*power_number(num, power-1)


print(power_number(2, 4))
