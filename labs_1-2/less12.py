

try:
    number = int(input("Введите число от -5 до 5: "))

    if number >= -5 and number <= 5:
        token = ""
        num_word = ""

        if number < 0:
            token = "минус "
            number *= -1

        match number:
            case 0:
                num_word = "ноль"
            case 1:
                num_word = "один"
            case 2:
                num_word = "два"
            case 3:
                num_word = "три"
            case 4:
                num_word = "четыре"
            case 5:
                num_word = "пять"

        print(token + num_word)
    else:
        print("Число вне диапазона!")

except ValueError:
    print("Вы ввели не число!")
