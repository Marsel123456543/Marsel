"Строки"
# строки - это не измянемый тип данных, предназаченный для хранения текста(последовательности символов)

string1 = 'строка в одинарных кавычках'
sting2 = "строка в двойных кавычках"
string3 = "Don't"
string4 = 'Study in "Makers Incubator"'
string5 = '''
Многострочный 
текст
тут можно использовать 'любые' "кавычки"
'''
string6= """
Тоже самое
"""
string7 = 'hello ' + ' world' # 'hello world'
string8 = 'hello' * 3 # 'hellohellohello'
stringe9 = 'hello' + str(1) # 'hello1'

"Экранизация строк"
'\n' # перенос на новую строку
'\t' # отступ (табуляция)
'\\' # отображение \
'\'' # отображение символа '
"\"" # отображение символа " 
'\r' # перенос каретки на начало строки
'\v' # перенос на новую строку со смещением направо на длину предыдущей строки

'helllo\nworld'
# hello
# world

'hello\tworld'
# hello    world 

'экранизация \\' 
# экранизация \ 

'hello\vworld\vmakers'
# hello
#       world
#             makers
 

"Индексы"
# индекс - порядковый номер символа в строке (начиная с 0) 
'h e l l o'
#0 1 2 3 4 

string = 'hello world'
string[0] # 'h'
string[-1] # 'd'
string[5] # ' ' 

# срез - часть строки 
string[6:9] # 'wor' 
string[0:5] # 'hello' 
string[0:6] # 'hello '
string[:6]  # 'hello'
string[:]   # 'hello world'
string[0:11:2] # 'hlowrd'
string[::2] # 'hlowrd' 


"Форматирование строк"
title = 'пирог'
price = 35
string = f'Название : {title}, цена: {price}'
# Название : пирог, цена: 35 

format = 'Название: %s, цена: %s'
print(format %("Яблоко", 80))
# Название: Яблоко, цена: 80 

format2 = 'Название: {}, цена: {}'
print(format2.format('Груша', 60))
# Название: Груша, цена: 60

"Методы строк"
# методы это функция, которая принадлежит определенному типу данных, обращаемся к ней через точку

dir(str) # посмотреть все доступные методы для данного типа данных

'hello' .upper() # 'HELLO'
'HELLO' .lower() # 'hello'

'hello WORLD' .swapcase() # 'HELLO world' 
'Hello' .swapcase() # 'hELLO'
'hello world' .title() # 'Hello World'
'hello world' .capitalize() # 'Hello world'

'hello' .center(11) # '   hello   ' 
'hello' .center(11, '-') # '---hello---'

'hello' .count('l') # 2 
'hello' .count('ll') # 1 
'Hello' .count('hello') # 0 
'hello' .count('') # 6 

'hello world' .split() # ['hello', 'world'] 
'hello world' .split('o') #['hell', 'w', 'rld']  

' '.join(['hello', 'world']) # 'hello world'
'%'.join(['hello', 'world']) # 'hello%world'

'hello world' .find('w') # 6
'hello world' .find('wor') # 6
'hello world' .find('o') # 4 
'hello world' .rfind('o') # 7
