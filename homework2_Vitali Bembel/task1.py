mrub, ncent, sqty = int(input("Введите рубли:\n ")), int(input("Введите копейки:\n ")), int(input("Кол. товара:\n "))

sumcent = ncent * sqty
sumrub = mrub * sqty
if sumcent >= 100:
    for count in range(sqty):
        sumrubcount = sumrub+count
        sumcentresidue = sumcent - (100*count)
else:
    sumrubcount = sumrub
    sumcentresidue = sumcent
print ("Общая цена: " + str(sumrubcount) + " руб. " + str(sumcentresidue) +" коп. за " + str(sqty) +" шт.")