result=''

ex1 = open("task51.txt", "r")
str1 = ex1.read()
ex1.close()

ex2 = open("task52.txt", "r")
str2 = ex2.read()
ex2.close()

mnogochlen1 = str1.split('+')
mnogochlen2 = str2.split('+')

koef_mnogochlen1 = []
koef_mnogochlen2 = []
som_res = ''

for i in range(0,len(mnogochlen1)):
    for x in mnogochlen1[i]:
       if x.isdigit():
        som_res+=x
       else:
        break
    if som_res=='':
        koef_mnogochlen1.append(0)    
    else:
        koef_mnogochlen1.append(som_res)
    som_res=''

print(mnogochlen1)
print(koef_mnogochlen1)

for i in range(0,len(mnogochlen2)):
    for x in mnogochlen2[i]:
       if x.isdigit():
        som_res+=x
       else:
        break
    if som_res=='':
        koef_mnogochlen2.append(0)    
    else:
        koef_mnogochlen2.append(som_res)
    som_res=''

print(mnogochlen2)
print(koef_mnogochlen2)
res_koef = []

for i in range(0,len(koef_mnogochlen1)):
    res_koef.append(int(koef_mnogochlen1[i])+int(koef_mnogochlen2[i]))
print(res_koef)

for i in range(0,len(res_koef)-1):
    if i != len(res_koef)-1:
        result+=(f'{str(res_koef[i])}x^{len(res_koef)-i-1}+')
    elif i == len(res_koef)-1:
        result+= (f'{str(res_koef[i])}x+')
result+=(f'{res_koef[-1]}=0')
print(result)

file = open("task5_res.txt", "w")
file.write(result)
file.close()