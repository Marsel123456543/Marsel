# print(5==5) -> True
# print(5==4) -> False

# "=" -> знак присвоения
# '== -> знак равенства


"Знак неравенства"
# print(4 != 5) -> True - это знак неравенства
# print(4 != 4) -> False


"Знак больше"
# print(5 > 5) ->  False
# print(5 > 4) ->  True


"знак меньше"
# print(5 < 4) -> False
# print(5 < 10) -> True 

"больше или ровно"
# print(5 >= 10) -> False
# print(5 >= 5) -> True 

"меньше или равно"
# print(5 <= 3) -> False
# print(5 <= 5) -> True

# print('5' == 5) -> False
# print('hello' == 'hello') -> True
# print('Hello' == 'hello') -> False


"=========== AND OR NOT ==========="
# and - и
# or  - или
# not - не

# a = 5
# b = 6

# print(a == 5 and b == 6) -> True
# print(a == 5 and b == 5) -> False 

# a = 5 
# b = 6

# print(a == 4 or b == 3) -> False
# print(a == 3 or b == 6) -> True

# print(not a == 5) -> False
# print(not a == 3 and not b == 6) -> False
# print(not a == 3 or not b == 6) -> True

# print (not True) -> False
# print (not False) -> True


"================= Boolean Type =================="
# у булево типа всего 2 значеиния: True и False

# print(bool(1)) -> True 
# print(bool(0)) -> False
# print(bool(-11)) -> True 
 
# print(bool('hello')) -> True 
# print(bool(' ')) -> True
# print(bool('')) -> False

# print(bool([])) -> False
# print(bool([[]])) -> True


"================== None Type ===================="
# None - неизменяемый тип данных с одним значением None,который используется для обохначениие пустоты
 
# print(bool(None)) -> False
# print(bool('None')) -> True

"================= Условные операторы ============"
# условные операторы - коснтрукция, которая используется для того, чтобы при разных входных данных код работал по-разному (в зависимости от условия)

#if условие1:
#    тело1
    # тело1 будет выполняться только если условие1 верно 
#else:
#    тело2
    # тело1 будет выполняться во всех других случаях

#if условие1:
#    тело1
    # тело1 будет выполняться только если условие1 верно 
#elif условие2:
#    тело2
    # тело2 будет выполняться только если условие1 не верное и если условие2 верное 


#if условие1:
#    тело1
    # тело1 будет выполняться только если условие1 верно 
#elif условие2:
#    тело2
    # тело2 будет выполняться только если условие1 не верное и если условие2 верное 
#else: 
#    тело3
    # тело3 будет выполняться во всех других случаях

# В одной конструкции мы можем использовать неограниченное количество elif или не использовать вообще 
# В одной конструкции мы можем использовать только один else или не использовать вообще 

#num = int(input('Введите число: '))

#if num > 0:
    #print(f'число {num} - положительное')

#elif num == 0:
    #print(f'число {num} - это 0')

#else:
    #print(f'число {num} - отрицательное')


#password = input('Придумайте пароль: ')
#first_let = password[0]

#if len(password) <= 8:
    #print('Ваш пароль меньше 8 символов')
#elif not password.startswith(first_let.upper()):
    #print('Ваш пароль не начинается с большой буквы') 


"Тернарные операнерторы"
# Тернарные операторы - условие в одну строку

#тело1 if условие else тело2 

#num = int(input())

#res = "Hello" if num == 5 else "Bye"
#print(res)

"FizzBuzz"
# примите число от пользователя 
# выведите Fizz, если число кратно 3
# выведите Buzz? если число кратно 5
# выевдите FizzBuzz, если число кратно и 3 и 5
# выведите само число во всех остальных случаях

num =int(input())
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num% 5 == 0:
    print('Buzz')
else:
    print(num)