# Задайте список из n чисел последовательности заполненный
# по формуле (1+1/n)**n и выведите на экран их сумму.

number = int(input('Введите число: '))
lis = list()
sum=0
for i in range(1, number+1):
   lis.append(round((1+1/i)**i))
   sum+=lis[i-1]
print(lis)
print(sum)