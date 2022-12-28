passwords = ['1114', '1782', '2039', '8829']

print("Список паролей:")
for password in passwords:
    print(password)

pswd = input("Введите свой пароль: ")

pswd_found = False

for el in passwords:
    if pswd == el:
        pswd_found = True
        break

if pswd_found:
    print("Пароль есть в списке")
else:
    print("Нет пароля списке")
