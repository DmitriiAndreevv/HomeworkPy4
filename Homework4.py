# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# n = float(input('введите число n: '))
# d = float(input('введите число d: '))
# if d == 1:
#     print(int(n))
# else:
#     d = str(d)
#     d = d.split('.')
#     d = len(d[1])
#     print(round(n, d))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('введите число: '))
# i = 2
# list1 = []
# num = n
# while i <= n:
#     if n % i == 0:
#         list1.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {num} приведены в списке: {list1}")

# Вариант 2

# n = int(input())
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             print(i)



# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# nlist = list(map(int, input('Введите числа через пробел: \n').split()))
# b = set(nlist)
# print([b])


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
# k = int(input('Введите натуральную степень k: '))
# coef = [random.randint(0, 100) for _ in range(k + 1)]
# print(coef)
# with open('coef.txt', 'w', encoding='utf-8') as m:
#     for i in range(len(coef)):
#         if k - i != 1 and k - i != 0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')
    


