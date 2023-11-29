#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    
    res = [max(A) if i == 0 else A[0] if num == max(A) else num for i, num in enumerate(A)]

    print("Преобразованный список: ", res)
