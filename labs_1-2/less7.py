
def multyply(num1, num2):
    return num1 * num2


try:
    a = float(input("Число 1: "))
    b = float(input("Число 2: "))

    if a >= 0 and b >= 0:
        print("Результат = ", multyply(a, b))
    else:
        print("Есть отрицательное число")
except ValueError:
    print("Не число")
