# Создайте пустой словарь.
# Запустите цикл который 3 раза спросит его имя и его пароль.
# Записывайте имя пользователя как ключ, а пароль как его значение

society = {}
count = 0
while count != 3:
    log = input('enter login: ')
    passw = input('enter password: ')
    society[log] = passw
    print(society)
    count += 1

