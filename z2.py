"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


def func_sort_sqr(x):            # O(N^2)
    for i in range(0, len(x) - 1):
        min_idx = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
        return x[0]


def func_sort_line(x):           # O(N)
    min_find = x[0]
    for i in x:
        if i < min_find:
            min_find = i
    return min_find


list_unsort = [1, 0, 3, 6, -5, 7]
print(func_sort_line(list_unsort))
print(func_sort_sqr(list_unsort))
