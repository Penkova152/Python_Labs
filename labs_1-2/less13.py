
import random

rand_num = random.randint(0, 10)
guessed_right = False


for i in range(3):
    print(f"  Попытка {i+1}. ", end="")
    yours_num = int(input("Введите число: "))
    guessed_right = (yours_num == rand_num)
    if guessed_right:
        break

if guessed_right:
    print("Вы угадали число")
else:
    print("неправильно. Правильное число:", rand_num)
