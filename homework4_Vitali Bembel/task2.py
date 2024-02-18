# 2.	Города
# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
# в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны. В следующей строке записано число M, далее идут M запросов —
# названия каких-то M городов, перечисленных выше.
#
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.
# Примеры
#
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
#
#
# 3
# Odessa
# Moscow
# Novgorod
#
# Выходные данные
# Ukraine
# Russia
# Russia


def find_country(city_stored, city):
    for country, cities in city_stored.items():
        if city in cities:
            return country
    return "Город не найден"

city_store = {}

qtycountry = int(input("Введите количество стран: "))

for i in range(qtycountry):
    cities = input("Введите название страны: ").split()
    country = input("Введите название города: ")
    for city in cities:
        city_store[city] = country

print(city_store)

qty_input_cities = int(input("Введите количество городов: "))
input_cities = [input("Введите название городов: ") for _ in range(qty_input_cities)]

for input_city in input_cities:
    print(find_country(city_store, input_city))
