# -*- coding: utf-8 -*-
"""
Задание 6.1

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX Однако, в оборудовании Cisco
MAC-адреса используются в формате XXXX.XXXX.XXXX

Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый
список result.
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

mac1 = mac[0]
mac2 = mac[1]
mac3 = mac[2]
mac4 = mac[3]

mac1 = mac1.replace(':', ".")
mac2 = mac2.replace(':', ".")
mac3 = mac3.replace(':', ".")
mac4 = mac4.replace(':', ".")

result = []
result.append(mac1)
result.append(mac2)
result.append(mac3)
result.append(mac4)
print(result)