# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Введите вещественное число: '))
while (number-int(number) != 0):
    number *= 10
result = 0
number = int(number)
while (number != 0):
    result += number % 10
    number //= 10
print(result)
