#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
N = int(input('Введите чило: '))
factorial = []
I=1
fact = 1
while I != N+1:
    fact *= I
    factorial.append(fact)
    I+=1
print(f'Набор произведений чисел от 1 до {N} {factorial}')
