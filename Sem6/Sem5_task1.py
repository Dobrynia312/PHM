#исключение слов с "абв"
l1 = ' '.join(list(filter(lambda x: 'абв' not in x, input().split())))
print(l1)

