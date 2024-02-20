m_rub, n_cent, s_qty = int(input("Введите рубли:\n ")), int(input("Введите копейки:\n ")), int(input("Кол. товара:\n "))

sum_cent = n_cent * s_qty
sum_rub = m_rub * s_qty
if sum_cent >= 100:
    for count in range(s_qty):
        sum_rub_count = sum_rub+count
        sum_cent_residue = sum_cent - (100 * count)
else:
    sum_rub_count = sum_rub
    sum_cent_residue = sum_cent
print ("Общая цена: " + str(sum_rub_count) + " руб. " + str(sum_cent_residue) +" коп. за " + str(s_qty) +" шт.")