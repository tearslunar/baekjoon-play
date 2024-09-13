import sys
import collections
input = sys.stdin.readline

n = int(input())
jux = dict()
juy = dict()
count = 0
for i in range(n):
    a, b = map(int, input().split())
    if not a in jux:
        jux[a] = 1
    else:
        jux[a] += 1

    if not b in juy:
        juy[b] = 1
    else:
        juy[b] += 1

for i in jux:
    if jux[i] > 1:
        count += 1
for i in juy:
    if juy[i] > 1:
        count += 1

print(count)

    