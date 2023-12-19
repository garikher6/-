# -*- coding: utf-8 -*-
"""
    Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_network = input("Введите IP-сеть в формате x.x.x.x/x: ")
network, mask = ip_network.split('/')
octets = network.split('.')
binary_mask = "1" * int(mask) + "0" * (32 - int(mask))

# Преобразование адреса хоста в адрес сети, если введен адрес хоста
if int(mask) < 32:
    host_address = octets
    host_binary = ''.join([bin(int(octet))[2:].zfill(8) for octet in host_address])
    network_binary = host_binary[:int(mask)] + '0' * (32 - int(mask))
    octets = [int(network_binary[i:i+8], 2) for i in range(0, 32, 8)]
print("Network:\n"
      f"{octets[0]:<10} {octets[1]:<10} {octets[2]:<10} {octets[3]:<10}\n"
      f"{int(octets[0]):08b}  {int(octets[1]):08b}  {int(octets[2]):08b}  {int(octets[3]):08b}\n\n"
      "Mask:\n"
      f"/{mask}\n"
      f"{int(binary_mask[0:8], 2):<10} {int(binary_mask[8:16], 2):<10} {int(binary_mask[16:24], 2):<10} {int(binary_mask[24:32], 2):<10}\n"
      f"{int(binary_mask[0:8], 2):08b}  {int(binary_mask[8:16], 2):08b}  {int(binary_mask[16:24], 2):08b}  {int(binary_mask[24:32], 2):08b}")