
try:
    num = int(input("Введите целое число: "))
    i = 1
    while i <= num:
        print(i * i)
        i += 1

except ValueError:
    print("Вы ввели не целое число")
