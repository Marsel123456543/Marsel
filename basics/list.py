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


