import sys
input = sys.stdin.readline
n, m = map(int, input().split())
b = dict()
di = dict()
for i in range(n):
    a = input().strip("\n")
    di[a] = i+1
    b[i+1] = a
for _ in range(m):
    a = input().strip("\n")
    if a.isnumeric() == False:
        print(di[a])
    else:
        print(b[int(a)])
