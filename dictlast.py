# Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
# С помощь цикла for пройти вывести на экран строку:
# "Здравствуйте <Имя>  Прекрасная профессия <Профессия>"

prof = {'Baha': 'programmer', 'Janar': 'krasavchik', 'Atai': 'fermer', 'Bektur': 'programmer', 'Nurbek': 'taxist'}

for i,j in prof.items():
    print("Здравствуйте ", i, "Прекрасная профессия ", j)
