# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
numbers = []
n = int(input('Введите длинну массива: '))
for i in range (n):
    numbers.append(random.randint(1,100))
print(numbers)
min = int(input('Введите нижнюю границу диапазона: '))
max = int(input('Введите верхнюю границу диапазона: '))
items =[]
for i in range(len(numbers)):
    if min<numbers[i]<max :
        items.append(i)
print(items)

