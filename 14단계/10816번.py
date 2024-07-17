import sys
input = sys.stdin.readline

n  = int(input())

li = list(map(int, input().split()))
di = dict()

m = int(input())
ul = list(map(int, input().split()))

for i in li:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

for i in ul:
    if i in di:
        print(di[i], end=' ')
    else:
        print(0,end=' ')
