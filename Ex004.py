# Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элеиентов на указанных позициях (не индексах).

number = int(input('Введите количество элементов: '))
position1 = int(input('Введите позицию первого числа: '))
position2 = int(input('Введите позицию второго числа: '))
lis = list()
for i in range(-number, number+1):
   lis.append(i)
product=lis[position1-1]*lis[position2-1]
print(lis)
print(product)