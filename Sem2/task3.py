#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
N = int(input('Введите чило: '))
numbers = []
i = 1
while i <= N:
    numbers.append((1+1/i)**i)
    i+=1
print(f'Список последовательности {numbers}')
summa = 0
for item in numbers:
    summa += item
print(f'Сумма последовательности {summa}')