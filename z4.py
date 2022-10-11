"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import os
import hashlib


salt = str(os.urandom(32))
cache_pages = {}


def page_hash(x):
    if cache_pages.get(x):
        print(f'Данный адрес: {x} присутствует в кэше')
        print(cache_pages)
    else:
        hash_sum = hashlib.sha512(salt.encode() + x.encode()).hexdigest()
        cache_pages[x] = hash_sum
        print(cache_pages)


page_hash('https://mail.ru')
page_hash('https://tps.uz')
page_hash('https://mail.ru')
