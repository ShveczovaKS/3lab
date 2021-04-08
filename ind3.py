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
