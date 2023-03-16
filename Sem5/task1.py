l1 = input().split()
print(l1)
l2 = []
def check(string): return 'абв' in string


for i in range(0, len(l1)):
    if not check(l1[i]):
        l2.append(l1[i])
print(' '.join(l2))
