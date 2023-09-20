a = []

for j in range(9):
    for i in range(9):
        if len(a) < 9:
            a.append(int(input()))
            max = a[0]
    if a[j] > max:
        max  = a[j]

print(max)
print(a.index(max) + 1)

#max,min함수안씀