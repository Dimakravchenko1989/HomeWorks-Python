# Задача 4. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

#Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float (input('Введите координаты точки А x1: '))
y1 = float (input('Введите координаты точки А y1: '))
x2 = float (input('Введите координаты точки В x2: '))
y2 = float (input('Введите координаты точки В y2: '))

katet1 = x1 - x2
katet2 = y1 - y2
gipotenusa = round((katet1 * katet1 + katet2 * katet2)**0.5,2)
print('Расстояние между точками А и В =', gipotenusa)