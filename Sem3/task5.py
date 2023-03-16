#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. 
def Fibonachi(N):
    if N == 1 or N == -1:
        return 1
    elif N == 0:
        return 0
    else:
        if N > 0:
            return Fibonachi(N-1) + Fibonachi(N-2)
        elif N < 0:
            return Fibonachi(N+2) - Fibonachi(N+1)

X = int(input())
fib_numb = []
for i in range(-X,X+1):
    fib_numb.append(Fibonachi(i))
print(fib_numb)
