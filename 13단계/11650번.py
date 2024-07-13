n = int(input())
li = []

for i in range(n):
    a, b = int(input().split())
    li.append([b, a])

li.sort()

for i in range(n):
    print(li[i][1], li[i][0])