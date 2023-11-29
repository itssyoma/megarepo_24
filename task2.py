#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    A = list(map(float, input("Введите элементы массива через пробел: ").split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    sum_negative = 0
    min_index = A.index(min(A))
    max_index = A.index(max(A))

    if min_index < max_index:
        rng = [i for i in range(min_index+1, max_index)]
    else:
        rng = [i for i in range(max_index+1, min_index)]

    product_between = 1
    for i, num in enumerate(A):
        if num < 0:
            sum_negative += A[i]
        if i in rng:
            product_between *= num

    A.sort()

    print("Сумма отрицательных элементов: ", sum_negative)
    print("Произведение элементов между максимальным и минимальным: ", product_between)
    print("Упорядоченный список: ", A)
