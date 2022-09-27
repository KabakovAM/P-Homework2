# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.

number = int(input('Введите натуральное число: '))
result = 1
lis = list()
for i in range(1, number+1):
    result *= i
    lis.append(result)
print(lis)
