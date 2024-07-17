import sys

n = int(sys.stdin.readline())
li = set(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
ul = set(map(int, sys.stdin.readline().split()))

for i in ul:
    if i in (li & ul):
        print(1, end=' ')
    else:
        print(0, end=' ')

#집합