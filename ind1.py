#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    n = int(input("n = "))
    if n > 10:
        print("Ошибка", file=sys.stderr)
        exit(1)
    if n == 1:
        b = " карандаш"
    elif n <= 4:
        b = " карандаша"
    else:
        b = " карандашей"
    print("Я купила ", n, b)