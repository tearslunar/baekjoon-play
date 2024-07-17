import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = set()
ul = []
pl = 0

for i in range(n):
    li.add(str(input()))
for i in range(m):
    if str(input()) in li:
        pl += 1

print(pl)