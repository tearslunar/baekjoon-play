n = int(input())
li = []
for i in range(n):
    li.append(str(input()))
li = list(set(li))
li.sort()
li.sort(key=len) # key = len
for i in li:
    print(i)