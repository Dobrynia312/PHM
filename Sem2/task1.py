#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
N = float(input('Введите чило: '))
X = N
while N != int(N):
       N *= 10
sum_numbers = 0
while N > 0:
    sum_numbers += N % 10
    N //= 10
print(f'Сумма цифрв в числе {X} равна {sum_numbers}')
