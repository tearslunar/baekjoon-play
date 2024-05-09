n = int(input())
s = []

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            s.append(i)
            n = n // i
            break
print(*s, sep="\n")
            