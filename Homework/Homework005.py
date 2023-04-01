# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def get_root(a, b):
#     if b == 1:
#         return a
#     return a * get_root(a, b - 1)

# num1 = int(input('Input a number1: '))
# num2 = int(input('Input a number2: '))
# print(get_root(num1, num2))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def get_sum(a, b):
    if a == 0:
        return b
    return get_sum(a - 1, b + 1)

num1 = int(input('Input a number1: '))
num2 = int(input('Input a number2: '))
print(get_sum(num1, num2))