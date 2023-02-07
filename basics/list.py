"List"
# список - это изменяемый, итегрируемый, индексипуемый и упорядочный тип данных, предназначенный для хранения элементов в строгом порядке.

list1 = [1, 3.5, 'hello', [1,2,3],(1,2), None, True, False]

list1[0] #10
list1[3] # [1,2,3]
list1[3][-1] #3
# sublist = list[3] # [1,2,3]
# sub list[-1] # 3
list1[-1] # False
list1[2][-1] #'o'

list2 = list('hello')
print(list2) # ['h', 'e', 'l', 'l', 'o']

list3 = list(range(3,10,2))
print(list3) # [3,5,7,9]
print(list(range(5))) # [0,1,2,3,4]


"изменяемость"
string = 'hello'
res = string.upper()
print(string) #'hello'
print(res) # 'HELLO'

list4 = []
list4.append(1)
list4.append(2)
list4.append(3)
print(list4) # [1, 2, 3]


"Методы списков"
# append - метод, кототрый добавляет элемент в конец списка 
list5 = []
list5.append('hello')
list5.append(500)
list5.append([1,2,3])
print(list5) # ['hello', 500, [1, 2, 3]]

# remove - метод, который удаляет елемент из списка по значению, но только первого вхождения этого элемента, выдаст ошибку ValueError, если такого элемента нет в списке 
list6 = ['hello', 500, 'worid', 1000, 'hello', 500]
list6.remove('hello')
print(list6) # [500, 'worid', 1000, 'hello', 500]

# pop - метод, который удаляет элемент из списка по индексу. если этого числа нет, выдаст IndexError
list7 = [10, 20, 30, 40, 50]
list7.pop() # удаление с конца
print(list7) #[10,20,30,40]

# также метод pop возвращает удаленный элемент
list8 = [10, 20, 30, 40, 50]
popped = list8.pop(0)
print(list8) # [20, 30, 40, 50]
print(popped) # 10

# list5 = []
# list5.pop()
# IndexError: pop from empty list


# insert - метод, который добавляет элемент в список по индексу 
list9 = [1,2,3,4]
list9.insert(0, 'hello')
print(list9) # ['hello', 1, 2, 3, 4]


# создайте список с числами от 1 до 10
# выведите список с числами в обратном порядке 
list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = list(range(1,11))
# print(list1[::-1])
# list1.reverse()
# print(list(reversed(list1)))
str="1 2 3 4 5 6 7 8 9 10" 
slicedString=str[::-1]
print (slicedString)

# clear - чистит список
list1 = [1,2,3,4]
list1.clear()
print(list1) # []

# count - считает кол-во элемента, который передаем в метод в списке
list1 = [1,2,3,4,1,2,1,4,1,6]
list1.count(1) # 4
list1.count(3) # 1
list1.count('hello') # 0

list1 = ['hello', 'hello', 'hello']
list1.count('hello') # 3
list1.count('l') # 0

list1 = [11, 12, 13]
list1.count(1) # 0

# index - возвращает индекс данного элемента
list2 = ['hello', 'world', 'makers']
ind = list2.index('hello')
print(ind) # 0
list2.index('makers') # 2

# sort - метод, который сортирует по возрастанию
# если передать .sort(reverse=True), то сортирует по убыванию
list3 = [34,12,67,12,89,45]
list3.sort()
print(list3) # [12, 12, 34, 45, 67, 89]
list3.sort(reverse=True)
print(list3) # [89, 67, 45, 34, 12, 12]
# list3.sort()
# list3.reverse()

list4 = ['a', 'c', 'b', 'B', 'A']
list4.sort()
print(list4) # ['A', 'B', 'a', 'b', 'c']

list5 = [10, 'b', 3, 'c', 5]
# list5.sort() 
# TypeError: '<' not supported between instances of 'str' and 'int'

# copy - возвращает копию списка
list1 = [1,2,3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)

# extend - расширяет список другим списком
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# list1.append(list2)
# list1  [1,2,3,4, [5,6,7,8]]

list1.extend(list2)
# list1  [1,2,3,4,5,6,7,8]