sum = []

for i in range(10):
    a = int(input())
    b = a%42
    sum.append(b)
    if sum.count(b) >= 2:
        sum.remove(b)

print(len(sum))