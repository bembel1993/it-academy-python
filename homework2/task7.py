import math

a = int(input("Введите сторону a :\n "))
b = int(input("Введите сторону b :\n "))
c = int(input("Введите сторону c :\n "))
if a==b==c:
    print ("Равносторонний треугольник")
    s = (a+b+c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Площадь треугольника: " + str(area))
elif (a and (b==c)) or (b and (a==c)) or (c and (a==b)):
    print ("Две стороны треугольника равны")
    s = (a+b+c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Площадь треугольника: " + str(area))
elif a != b or b !=c or c!=a:
    print("Данные введены неверно")




