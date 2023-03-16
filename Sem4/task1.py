#Вычислить число c заданной точностью d
import math
d = float(input('Введите точность '))
x = str(math.pi)
f = 1
if d == 1:
    print(int(math.pi))
else:
    while d != int(d):
        d *= 10
        f+=1
    print(x[:1+f])