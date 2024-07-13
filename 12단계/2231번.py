n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
    for j in range(len(str(i))):
        sum += int(str(i)[j])

    if sum == n:
        print(i)
        break
    elif i == n:
        print(0)

    sum = 0