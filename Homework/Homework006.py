# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def get_progression(a, d, n):
#     mylist = []
#     for i in range(n):
#         number = a + (n-1) * d
#         mylist.append(number)
#         a -= d
#     print(sorted(mylist))



# first_element = int(input('Input your first element:'))
# step = int(input('Input your step: '))
# quantity = int(input('Input your quantity: '))
# get_progression(first_element, step, quantity)

#Эталонное решение:

# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)

def find_indeces(new_array):
    min_d = int(input('Input a min diaposon: '))
    max_d = int(input('Input a max diaposon: '))
    new_list = []
    for i in range(len(new_array)):
        if min_d <= new_array[i] <= max_d:
            new_list.append(i)
    print(new_list)

mylist = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
find_indeces(mylist)

#Эталонное решение:

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)