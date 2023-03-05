# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только
# +1 и -1. Также нельзя использовать циклы.
# 2 2 -> 4
import sys

from addInterface import correct_int


def summa_ab(num_a: int, num_b: int):
    if num_b == 0:
        return num_a
    if num_b > 0:
        return num_a + summa_ab(1, num_b - 1)


print(sys.getrecursionlimit())           # Предел глубины рекурсии - число
print("Введите первое число: ", end="")  # применений функции внутри функции
num_1 = correct_int()                    # не может превышать этого числа.
print("Введите второе число: ", end="")  # Согласно этому, второй параметр в
num_2 = correct_int()                    # summa_ab() не может быть больше 998
if num_2 > 998:
    num_2 = 998
num_res = summa_ab(num_1, num_2)
print(f"Сумма чисел {num_1} и {num_2} равна {num_res}")
