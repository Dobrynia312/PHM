#Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
from random import randint

N = [1,4,6,8,5,7]
print(N)
for i in range(0,len(N)//2):
    ind = randint(0,len(N)-1)
    N[i], N[ind] = N[ind], N[i] 
print(N)

