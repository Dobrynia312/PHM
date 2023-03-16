#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
N = int(input('Введите чило: '))

numbers = list(map(lambda i: (1+1/i)**i,[i for i in range(1,N+1)]))
print(f'Список последовательности {numbers}')

summa = sum(numbers)
print(f'Сумма последовательности {summa}')