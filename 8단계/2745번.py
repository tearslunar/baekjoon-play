a, b = input().split()
sets = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0
d = 0

for i in range(len(a)-1, -1, -1):
    c = sets.index(a[i])
    sum += c * (int(b)**d)
    d += 1

print(sum)