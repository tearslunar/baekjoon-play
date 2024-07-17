import sys
input = sys.stdin.readline

n = int(input())
di = {}
li = []
for _ in range(n):
    a, b = map(str, input().split())
    di[a] = b

for i in di:
    if di[i] == 'enter':
        li.append(i)
li.sort(reverse=True)

print(*li, sep="\n") 