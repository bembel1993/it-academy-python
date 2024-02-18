# 1.	Dict comprehensions
# Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
# а значениями кубы этих чисел.

def dict_comprehensions(rang):
    dict = {i : i**3 for i, v in enumerate(range(rang))}

    return dict

a = 10

print(dict_comprehensions(a))