#Homework "РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ"
#DZIANIS MASHKOVICH
#17.03.2024

#Exercise #1
"""
Вам дана строка. Выведите все подстроки, содержащие "cat".
"""

import re
pattern = r"cat"
line = "rassoftcatmyhomecat"
print (re.findall(pattern, line))

#Exercise #2
"""
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
"""

import re
pattern = r'z\d\d\dz'
line = "sdd456 kdj34 z445z ffg3888dd s332s z477z"
print(re.findall(pattern, line))

#Exercise #3
"""
3) Номер должен быть длиной 10 знаков и начинаться с 8 или 9.
Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python
"""

pattern = r'[8-9]\d{9}'
list = '6543453215 5674346783 8666666666 9000865434'
print(re.findall(pattern, list))

#Exercise #4
"""
Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
"""

import re
pattern = r'\s[aeiouy].{1,}\s'
list = 'David samon anny old town'
print(re.findall(pattern, list))

#Exercise #6
"""
В каждой строке замените все вхождения подстроки
"human" на подстроку "computer" и выведите полученные строки.
"""

import re
pattern = r'human'
repl = 'computer'
list = 'same dollar human old town Minsk human slack'
print(f'До замены: {list}')
print (f'После замены: {re.sub(pattern, repl, list, count=0)}')

#Exercise #7
"""
Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28).
"""

import re
pattern = r'\s\d{4}\-\d{2}\-\d{2}'
list = '20000-05-044 2022-02-28 2023-03-29 DZIANIS somelist'
print(re.findall(pattern, list))

#Exercise #8
"""
Найти все слова, в которых есть хотя бы одна буква ‘b’
"""

import re
pattern = r'\w*b\w*'
list = 'asram frodo beggins color home visa  borimor mazda orbitrazh mercedes'
print (re.findall(pattern, list))

#Exercise #9
"""
В каждой строке замените все вхождения нескольких одинаковых букв
на одну букву. Буквой считается символ из группы 
"""

import re
pattern = r'(\w)\1+'
repl = 'M'
list = r'Anna Smmaa Suhar summer metbkr mmmaa'
print(re.findall(pattern, list))
print(re.sub(pattern, repl, list, count=0))

#Exercise #10
"""
Поиск URL. Это регулярное выражение находит URL-адреса,
начинающиеся с "http://" или "https://", далее допускается "www." (опционально),
за которым следует доменное имя, а затем дополнительный путь и параметры.
"""
#написал под две youtube-ссылки
import re
pattern = r'\w*[p,s]://w{3}\.[A-Za-z0-9]+\.\w*/\D*[=?]+\w*'
list = 'httopp//fjfhjkdlld https://www.onliner.by https://beseller.by/blog/redirekty/ https://www.youtube.com/watch?v=hXyLAB72YBI https://www.youtube.com/watch?v=qnOj7IXNuME http://twitter.com fhfgdkdjjdd'
print(re.findall(pattern, list))

#Exercise #11
"""
Напишите регулярное выражение для поиска всех HTML тегов в тексте
"""

import re
pattern = r'\<+[A-Za-z0-9!\s+]+\>'
list = ' <html> <head> <title> рараоао <!DOCTYPE html>Событие source onmessage <meta name> initial-scale=1'
print (re.findall(pattern,list))
