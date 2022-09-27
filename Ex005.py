# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

import random
number = int(input('Введите число: '))
lis = list()
lis_of_index = list()
new_lis = list()
new_lis_of_index = list()

for i in range(number):
   lis.append(i)

for i in range(len(lis)):
   lis_of_index.append(i)
new_lis_of_index = random.sample(lis_of_index, len(lis))
for i in range(len(lis)):
   for j in range(len(lis)):
      if (i == new_lis_of_index[j]):
         new_lis.append(lis[j])
print(lis)
print(new_lis)
