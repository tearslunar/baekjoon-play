import sys
input  = sys.stdin.readline
n, m = map(int, input().split())
li = []
ul = []
for _ in range(n):
    li.append(input().rstrip("\n"))
for _ in range(m):
    ul.append(input().rstrip("\n"))

li = set(li)
ul = set(ul)

print(len(li & ul))
print(*sorted(li & ul), sep="\n")