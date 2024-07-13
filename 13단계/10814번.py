a = int(input())
n = [input().split() for _ in range(a)]

print(n)
for i in range(len(n)):
    n[i][0] = int(n[i][0])

n.sort(key=lambda x : x[0])
for i in range(len(n)):
    print(*n[i])