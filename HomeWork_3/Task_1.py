# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = int(input('Введите размер списка: '))
list = []
sum = 0
for i in range(n):
    list_n = int(input(f'Введите элемемент {i+1}: '))
    list.append(list_n)
    if i % 2 != 0:
        sum += list[i]


print(list)
print(f'Сумма элементов на нечетных позициях: {sum}')
