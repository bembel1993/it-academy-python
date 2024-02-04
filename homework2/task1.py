from math import sqrt

Mrub, Ncent, Sqty = int(input("Введите рубли:\n ")), int(input("Введите копейки:\n ")), int(input("Кол. товара:\n "))

sumcent = Ncent * Sqty
sumrub = Mrub * Sqty
if sumcent >= 100:
    for count in range(Sqty):
        sumrubcount = sumrub+count
        sumcentresidue = sumcent - (100*count)
else:
    sumrubcount = sumrub
    sumcentresidue = sumcent
print ("Общая цена: " + str(sumrubcount) + " руб. " + str(sumcentresidue) +" коп. за " + str(Sqty) +" шт.")