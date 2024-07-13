n = str(input())
li = []

for i in range(len(n)):
    li.append(n[i])

li.sort(reverse=True)

print(*li, sep='')