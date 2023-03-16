#Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
#многочлена и записать в файл многочлен степени k.
import random


k = int(input('Введите натуральную степень: '))
koef = []
ixi = []
res = []
str_res=''
while k > -1:
    if k > 1:
        koef.append(random.randint(0,101))
        ixi.append(f'x^{k}')
    elif k == 1:
        koef.append(random.randint(0,101))
        ixi.append(f'x')
    elif k == 0:
        koef.append(random.randint(0,101))
        ixi.append('')
    k-=1
for i in range(0,len(koef)):
    if koef[i] == 1 and i<len(koef)-1:
        res.append(ixi[i])
    elif koef[i] == 0:
        continue
    res.append(str(koef[i])+(ixi[i]))
    if ixi[i] == '':
        continue
for i in range(0,len(res)):
    if i < len(res)-1:
        str_res+=str(res[i])+'+'
    elif i == len(res)-1:
        str_res+=str(res[i])+'=0'
file = open("test.txt", "w")
file.write(str_res)
file.close()