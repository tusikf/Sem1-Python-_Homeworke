# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
n = int(input('Введите положительное число:'))
k = 0
stepen = 1
list = [1]

while stepen < n/2:
    stepen *= 2
    k += 1
    list.append(stepen)
print(f" 2 в степени меньше загаданного {n}, значение степени: {list}")
