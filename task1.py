"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, 
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""
n = int(input("Введите количество элементов в первом наборе: "))
list1=[]
for i in range(n):
    num = int(input("Введите число для первого набора: "))
    list1.append(num)
print(list1)


m = int(input("Введите количество элементов во втором наборе: "))
list2 = []
for i in range(m):
    num = int(input("Введите число для второго набора: "))
    list2.append(num)
print(list2)

reslist = []
for i in list1:
    for j in list2:
        if i == j:
            reslist.append(i)
result = sorted(list(set(reslist)))
print(*result)        