#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
N = int(input('Введите натуральное число '))
mnj = []
while N < 0:
    print('Это не натуральное число')
    N = int(input('Введите натуральное число '))
x = 2
while x * x <= N:
    if N % x == 0:
        mnj.append(x)
        N//=x
    else:
        x+=1
if N >  1:
    mnj.append(N)
print(mnj)
