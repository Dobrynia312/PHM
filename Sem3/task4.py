#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
N = int(input("XX"))
d = []
while True:
    d.append(N%2)
    N = N//2
    if N//2 == 0 and N != 1:
        break
d.reverse()
print(d)