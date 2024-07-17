import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
ul = list(map(int, sys.stdin.readline().split()))

di = {}
for i in li:
    di[i] = 1

for i in ul:
    try:
        if di[i] == 1:
            print(1, end=' ')
    except KeyError:
        print(0,end=' ')