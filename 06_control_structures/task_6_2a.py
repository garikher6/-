# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input('Введите IP-адрес: ')

octets = ip_address.split('.')

if len(octets) != 4:
    print('Неправильный IP-адрес')
else:
    correct_format = True
    for octet in octets:
        if not octet.isdigit():
            correct_format = False
            break
        if not 0 <= int(octet) <= 255:
            correct_format = False
            break
    if not correct_format:
        print('Неправильный IP-адрес')
    else:
        first_octet = int(octets[0])

        if ip_address == '255.255.255.255':
            print('local broadcast')
        elif ip_address == '0.0.0.0':
            print('unassigned')
        elif 1 <= first_octet <= 223:
            print('unicast')
        elif 224 <= first_octet <= 239:
            print('multicast')
        else:
            print('unused')
            