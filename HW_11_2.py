# Задача 2. Имеются данные о площади и стоимости 15 домов. Риелтору требуется узнать в каких домах стоимость 
# квадратного метра меньше 50000 рублей. Предоставьте ему графические данные о стоимость квадратного метра 
# каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import matplotlib.pyplot as mat
import random

house_list = list(random.randint(100, 300) for i in range(15))
price_list = list(random.randint(3, 20) for i in range(15))
metr_price_list = list(map(lambda x, y: round((x/y)*1000000, 2), price_list, house_list))
house_numbers = list(i for i in range(15))
line = [50000]*15

print(f'Площади имеющихся домов {house_list} кв. м.')
print(f'Стоимости имеющихся домов {price_list} млн. руб.')
print(f'стоимость квадратного метра имеющихся домов {metr_price_list} руб. за кв. м.')

new_list = []
for i in range(15):
    if metr_price_list[i] < 50000:
        new_list.append(house_list[i]) 
# new_list = new_list.sort() - почему-то не работает метод сортировки. Выводится None
print(f'Площади подходящих по стоимости домов: {new_list} кв. м.')

mat.bar(house_numbers, metr_price_list)
mat.plot(line, "r-")
mat.show()
