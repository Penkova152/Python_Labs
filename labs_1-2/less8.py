import random


def multyply(num1, num2):
    return num1 * num2


try:
    num = float(input("Введите число больше пяти: "))
    rand = random.randint(0, 6)

    if num > 5:
        print("Случайное число:", rand)
        print("Результат:", multyply(rand, num))
    else:
        print("число меньше или равно пяти")

except ValueError:
    print("Вы ввели не число")
