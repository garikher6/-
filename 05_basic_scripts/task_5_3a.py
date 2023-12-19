# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

inter = input("выберите интерфейс(access/trunk):")
typ = input("Введите тип и номер интерфейса:")


if inter == "access" :
    vlan = input("Введите номер VLAN")
    print("interface", typ)
    print("switchport mode access",
    f"switchport access vlan {vlan}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable", sep =("\n"))
elif inter == "trunk":
    vlan = input("Введите разрешенные VLANы:")
    print("interface", typ)
    print("switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    f"switchport trunk allowed vlan {vlan}", sep=("\n"))