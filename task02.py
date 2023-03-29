import os
os.system('cls')

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [int(input(f"Введите элемент массива {i + 1}: ")) for i in range(int(input("Введите длину массива: ")))]
min_el = int(input('Введите минимальный элемент: '))
max_el = int(input('Введите максимальный элемент: '))
if min_el >= max_el:
    min_el, max_el = max_el, min_el
print(list_1)
print(f'{min_el} ... {max_el}')
for i in range(len(list_1)):
    if min_el <= list_1[i] <= max_el:
        print(i, end= ' ')