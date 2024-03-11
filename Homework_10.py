#10.03.2024, Mashkovich Dzianis

# Exercise №1
"""
Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных,
и функцию которая находит наибольшее значение из этих двух переменных.
"""

class Main:
    def __init__(self, num_1: int, num_2: int):
        self.num_1 = num_1
        self.num_2 = num_2
    def prin (self):
        print(self.num_1)
        print(self.num_2)
    def izm (self):
        self.num_1 = 11
        self.num_2 = 14
        print(self.num_1)
        print(self.num_2)
    def sum (self):
        a = self.num_1 + self.num_2
        print(a)
    def max (self):
        if self.num_1 > self.num_2:
            print(f'Max: {self.num_1}')
        if self.num_2 > self.num_1:
            print(f'Max: {self.num_2}')
        if self.num_1 == self.num_2:
            print(f'Значения равны')
if __name__ == '__main__':
    t = Main (10, 12)
    t.prin()
    t.izm()
    t.sum()
    t.max()
# Exercise №2
"""
Описать класс, реализующий десятичный счетчик,
который может увеличивать или уменьшать свое
значение на единицу в заданном диапазоне. 
Предусмотреть инициализацию счетчика значениями по умолчанию
и произвольными значениями. Счетчик имеет два метода:
увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
Написать программу, демонстрирующую все возможности класса.
"""

class Count:
    def __init__(self, coun: int):
        self.coun = coun
        print('Предлагаем ознакомиться с работой десятичного счетчика!')
        print()
        print('ВНИМАНИЕ! Cчетчик записывает числа в десятичной системе счисления,')
        print('где каждый разряд имеет десять возможных значений от 0 до 9')
        print()
        print(f'ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ: {coun}')
    def proiz (self):
        print()
        print('ПРОИЗВОЛЬНОЕ ЗНАЧЕНИЕ')
        self.coun = int(input('Введите значение от 0 до 9: '))
        s.min()
        s.max()
    def min (self):
        if self.coun >= 0 and self.coun <= 9:
            a = self.coun - 1
            if a >=0 and a <=9:
                print(f'Текущее состояние счетчика в диапазоне уменьшения: {a}')
            else:
                print('Недопустимое значение')
    def max (self):
        if self.coun >= 0 and self.coun <= 9:
            b = self.coun + 1
            if b >= 0 and b <= 9:
                print(f'Текущее состояние счетчика в диапазоне уменьшения: {b}')
            else:
                print('Недопустимое значение')
if __name__== '__main__':
    s = Count(2)
    s.min()
    s.max()
    s.proiz()

# Exercise №3
"""
Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов,
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
"""


class Shop:
    def __init__(self):
        print('ГЛАВНАЯ СТРАНИЦА. БАЗА ДАННЫХ МАГАЗИНА ПРОДУКТОВ')
        print()
        print('ДЛЯ ЗАГРУЗКИ АКТУАЛЬНОЙ БАЗЫ ДАННЫХ (ПЕРВОЕ ИСПОЛЬЗОВАНИЕ) ВВЕДИТЕ ЦИФРУ - 1: ')
        print()
        print('Нажмите цифру: 2 - поиск продуктов в базе')
        print('Нажмите цифру: 3 - добавление продуктов в базу')
        print('Нажмите цифру: 4 - удаление продуктов из базы')
        print()
        print()
        another = int(2)
        another_2 = int (3)
        another_3 = int (4)
        another_4 = int(1)
        zap = int(input('Сделайте выбор: '))
        if another == zap:
            my_search = self.search()
        if another_2 == zap:
            my_add = self.add()
        if another_3 == zap:
            my_delete = self.delete()
        if another_4 == zap:
            my_loading = self.loading()
    def search (self):
        found = False
        file = open('shop.txt', 'r')
        search_shop = str(input('Введите значение поиска: '))
        strr = str(file.readline())
        while strr != '':
            strr = strr.rstrip('\n')
            if strr == search_shop:
                print(f'Найдено значение в базе: {strr}')
                found = True
            strr = file.readline()
        file.close()
        if not found:
            print('Это значение в базе не найдено')
    def add (self):
        file = open('shop.txt', 'a')
        another = 'HOME'
        add = str(input('Введите значение для ввода в базу, "HOME" - выход на главную страницу: '))
        while add != 'HOME' or add != 'HOME':
            if add != 'HOME':
                file.write(add + '\n')
                add = str(input('Введите значение для ввода в базу, "HOME" - выход на главную страницу: '))
            if add == 'HOME':
                Shop()
    def delete (self):
        import os
        found = False
        file = open('shop.txt', 'r')
        temp = open('temp.txt', 'w')
        delete = str(input('Введите значение для удаления: '))
        a = file.readline()
        while a != '':
            a = a.rstrip('\n')
            if a != delete:
                temp.write(f'{a}\n')
            else:
                found = True
            a = file.readline()
        os.remove('shop.txt')
        os.rename('temp.txt', 'shop.txt')
        if not found:
            print('Значение поиска не найдено в базе')
        else:
            print('Файл удален')
    def loading (self):
        file = open('shop.txt', 'w')
        global found
        data = ["Сыр", "Молоко", "Хлеб", "Колбаса", "Конфеты", "Соль", "Сода"]
        for item in data:
            file.write(item + "\n")
        file.close()
        print('Отлично! База данных подгружена')
        Shop()
if __name__ == '__main__':
    Shop()

# Exercise №4
"""
Реализуйте класс MoneyBox, для работы с
виртуальной копилкой.Каждая копилка имеет ограниченную вместимость, которая
выражается целым числом – количеством монет(capacity - вместимость), которые
можно положить в копилку.Класс должен поддерживать информацию о количестве
монет в копилке, предоставлять возможность добавлять монеты в копилку
и узнавать, можно ли добавить в копилку ещё какое - то количество монет, не
превышая ее вместимость. Класс должен иметь следующий вид:

class MoneyBox:
    def__init__(self, capacity):

    # конструктор с аргументом- вместимость копилки
    def can_add(self, v)

    # True, если можно добавить v монет, False иначе
    def add(self, v)


# положить v монет в копилку

При создании копилки, число монет в ней равно
0. Гарантируется, что метод add(self, v)
будет вызываться только если
can_add(self, v) – True.

"""
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return self.count + v <= self.capacity
    def add(self, v):
        if self.can_add(v):
            self.count += v
