"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def random_numb(x, att=10):
    if att > 0:
        user_numb = input(f'Загадано число от 1 до 100. У ваc {att} попыток. Введите число: ')
        try:
            if int(user_numb) > ran_numb:
                print('Неверно, загаданное число меньше')
                att -= 1
                return random_numb(ran_numb, att)
            elif int(user_numb) < ran_numb:
                print('Неверно, загаданное число больше')
                att -= 1
                return random_numb(ran_numb, att)
            else:
                return print('Вы угадали число')
        except ValueError:
            print('Вы ввели некорректное число')
            return random_numb(x, att)
    else:
        print(f'У вас не осталось попыток. Загаданное число было {ran_numb}')


(ran_numb) = (randint(1, 100))
random_numb(ran_numb)
