# Требуется найти в массиве A[1..N] самый близкий по величине элемент к 
# заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих строках записаны
#  N целых чисел Ai. Последняя строка содержит число X 5  1 2 3 4 5  6  -> 5
list1 = list()
n = int(input("Веедите длину массива "))
x = int(input("введите число x  " ))
for i in range(n):
    list1.insert(i, int(input("Введите числа массива: ")))
print(list1)
if list1[0] >= x:
    k = list1[0] - x
else:
    k = x - list1[0]
for j in range(1, len(list1)):
    if list1[j] >= x:
        if k >= list1[j] - x:
            k = list1[j] - x
            index = j
    else:
        if k >= x - list1[j]:
            k = x - list1[j]
            index = j
print(list1[index])
