 # Из Dictionary №1:
# Добавьте в меню  'besh_barmak' который стоит  130 сом.
# Оказалось лагман слишком дешевый. Обновите цену на 135
# Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
# Удалить borsh

menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['besh_barmak'] = 130 # create new dict
b = {'besh_barmak':135} #                   for add from menu
menu.update(b)          # add b to menu
menu.pop('borsh', 100)  # delete borsh
print(menu)

