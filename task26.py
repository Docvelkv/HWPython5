# Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую неотрицательную степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
from addInterface import correct_int


def a_pow_b(num_a: int, num_b: int):
    if num_b == 0:
        return 1
    if num_b == 1:
        return num_a
    else:
        return num_a * a_pow_b(num_a, num_b - 1)


print("Введите число: ", end="")
num_1 = correct_int()
print("Введите число степени: ", end="")
num_2 = correct_int()
num_res = a_pow_b(num_1, num_2)
print(f"Число {num_1} в степени {num_2} равно {num_res}")
