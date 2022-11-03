"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
import sys
from memory_profiler import profile


@profile
def numb_chen(x):
    n = x * 100
    a = [i for i in range(n + 1)]

    a[1] = 0
    i = 2

    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j += i
        i += 1

    b = [i for i in a if i != 0]
    print(sys.getrefcount(i))
    print(sys.getrefcount(a))
    return b, f'{x} по счету простое число: {b[x - 1]}'


idx = 100
numb_chen(idx)
