# (21 вариант) Ежемесячная стипендия студента составляет р., а расходы на проживание превышают стипендию и составляют р. в месяц. Рост цен ежемесячно увеличивает расходы на 3%. Составьте программу расчета необходимой суммы денег, которую надо единовременно просить у родителей, чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
grants = int(input("ежемесячная стипендия"))
expenses = int(input("ежемесячные расходы"))
months = 10
money = 0
ask_for_money = 0
while ask_for_money <= months - 1:
    money += expenses - grants
    expenses *= 1.03
    ask_for_money += 1
print("{0:.2f}".format(money))
