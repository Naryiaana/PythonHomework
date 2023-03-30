# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые 
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно 
# перевернуть

quantity = int(input('Input a quantity of coins: '))
amount1 = amount2 = 0
for i in range(quantity):
    coins = int(input('Input 0 or 1: '))
    if coins == 0:
        amount1 += 1
    else:
        amount2 += 1
if amount1 > amount2:
    print(f'The least amount of coins to flip is {amount2} ones')
else:
    print(f'The least amount of coins to flip is {amount1} zeroes')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Input a number: '))
result = 0
while (2 ** result < number):
    print(2 ** result)
    result += 1
    
                                                                                                                                                         
