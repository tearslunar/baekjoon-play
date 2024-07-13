import sys #시간초과

n = int(sys.stdin.readline())
li = []
for i in range(n):
    a = int(sys.stdin.readline())
    li.append(a)

li.sort()
for i in range(len(li)):
    print(int(li[i]))