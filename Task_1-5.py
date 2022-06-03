'''
1. Найти НОК двух чисел

2. Вычислить число Пи c заданной точностью d
   Пример: при d = 0.001,  c= 3.141. 

3. Составить список простых множителей натурального числа N

4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
   Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

+ на тему файловой системы:
5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
'''
# =================================================================================

# 1. Найти НОК двух чисел

from decimal import ROUND_FLOOR, Decimal
from math import lcm, pi
import math
from random import randint


def Finding_Least_Common_Multiple(a, b):
    return lcm(a, b)

A = int(input('Введите первое число:\n'))
B = int(input('Введите первое число:\n'))

print(f'НОК числа {A} и {B} => {Finding_Least_Common_Multiple(A, B)}')
  
# =================================================================================

# 2. Вычислить число Пи c заданной точностью d
#   Пример: при d = 0.001,  c= 3.141. 

A = input('Введите число для вычисления числа Пи с заданной точностью (Пример: А = 1.000):\n')
num = str(pi)
number = Decimal(num)
print(number.quantize(Decimal(A), ROUND_FLOOR))

# ================================================================================

# 3. Составить список простых множителей натурального числа N

def Prime_Factors(n):
    num_list = []
    while n % 2 == 0:
        num_list.append(2),
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while(n % i == 0):
            num_list.append(i)
            n = n / i
    if n > 2:
        print(n)
        num_list.append(n)
    return num_list

N = int(input('Введите натуральное число:\n'))
print(f'Список простых множителей натурального числа {N} равен {Prime_Factors(N)}')

# ================================================================================

# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#   Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

def List_non_repeating_Elements(list):
    return [i for i in set(list)]

origin_list = list(map(int, input('Введите через пробел числа:\n').split()))

print(List_non_repeating_Elements(origin_list))

# ================================================================================

# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

def main(n):
    with open('random.txt', 'w+') as ran:
        for _ in range(n):
            ran.write(f'{str(randint(1,100))}\n')

N = int(input('Сколько случайных чисел будет храниться в файле? \n'))
main(N)

read_list = []
with open('random.txt', 'r') as data:
    for i in data:
        if (int(i) % 2 != 0):
            read_list.append(int(i))

with open ('file.txt', 'w+') as file:
    for i in read_list:
        file.write(f'{str(i)}\n')