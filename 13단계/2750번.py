n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)

li.sort()
for i in range(len(li)):
    print(int(li[i]))