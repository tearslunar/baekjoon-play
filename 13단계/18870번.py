import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
ul = sorted(list(set(li)))
di = {}
for i in range(len(ul)):
    di[ul[i]] = i

for i in li:
    print(di[i], end=' ')