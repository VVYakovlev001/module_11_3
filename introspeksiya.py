import sys
import inspect

import numpy


class Info:
    def __init__(self,obj):
        self.obj = obj
        

def introspection_info(obj):
        pass



number_info = introspection_info(42)

rw = type(42)
rw1 = type(number_info)
rw2 = dir(number_info)
rw3 = id(number_info)
rw4 = inspect.getfile(numpy.dtype)

print(f' тип : {rw}, тип класса : {rw1} ,индикационный номер:{rw3},'
      f' Модуль к которому принадлежит: {rw4}')
print(f'атрибуты и методы: {rw2}')










'''     
 Необходимо создать функцию, которая принимает объект(любого типа) в качестве
 аргумента и проводит интроспекцию этого объекта, чтобы определить его
 тип, атрибуты, методы, модуль, и другие свойства.
1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения
 информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
 - Тип объекта.  - Атрибуты объекта. - Методы объекта. - Модуль, к которому объект
принадлежит. - Другие интересные свойства объекта, учитывая его тип(по желанию).
 Пример работы:
number_info = introspection_info(42)
print(number_info)
 Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...],
 'module': '__main__'}
 '''''
