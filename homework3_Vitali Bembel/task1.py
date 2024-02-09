# 1.	FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz


def fizz_buzz(number):
    b = []
    for x in range(1, number):
        if x % 3 == 0 and x % 5 ==0:
            b.append("FizzBuzz")
        elif x % 3 == 0:
            b.append("Fizz")
        elif x % 5 == 0:
            b.append("Buzz")
        else:
            b.append(x)
    return b

print(fizz_buzz(100))