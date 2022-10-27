"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
import collections


count_companies = int(input('Введите количество предприятий для расчета прибыли: '))

companies = []

for i in range(count_companies):
    title = input('Введите название предприятия: ')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('Квартальные прибыли через пробел: ').split(' '))
    company = {
        'Название предприятия': title,
        'Первый квартал': profit_q1,
        'Второй квартал': profit_q2,
        'Третий квартал': profit_q3,
        'Четвертый квартал': profit_q4,
        'Итого': profit_q1 + profit_q2 + profit_q3 + profit_q4,
    }

    companies.append(company)

profit_col = collections.Counter()
for company in companies:
    profit_comp = company.copy()
    del profit_comp['Название предприятия']
    profit_col += collections.Counter(profit_comp)

print()
for company in companies:
    print(company)

average_profit = profit_col['Итого'] / len(companies)

print('Суммарная прибыль предприятий: ', profit_col)
print('Средняя годовая прибыль предприятий: ', average_profit)
print('Прибыль выше среднего: ', [x['Название предприятия'] for x in companies if x['Итого'] >= average_profit])
print('Прибыль ниже среднего: ', [x['Название предприятия'] for x in companies if x['Итого'] < average_profit])

