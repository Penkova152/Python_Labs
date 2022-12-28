print("Введите 10 чисел: ")

numbers = []

for i in range(10):
    numbers.append(int(input(f"{i + 1} число = ")))

numbers.sort()

for num in numbers:
    print(num, end="; ")
