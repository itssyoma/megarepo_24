#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    
    max_elem = A[0]
    max_index = 0

    for i, num in enumerate(A):
        if num > max_elem:
            max_elem = num
            max_index = i

    A[0], A[max_index] = A[max_index], A[0]

    print("Преобразованный список: ", A)
