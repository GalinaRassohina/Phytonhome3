#Требуется вычислить, сколько раз встречается некоторое число X в 
# массиве A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих строках 
# записаны N целых чисел Ai. Последняя строка содержит число X
# 5    1 2 3 4 5   3    -> 1

list1 = list()
n = int(input("Веедите длину массива "))
x = int(input("введите число x  " ))
k = 0
for i in range(n):
    list1.insert(i, int(input("Введите числа массива: ")))
print(list1)
for j in list1:
   if j == x:
    k+=1
print(k)        