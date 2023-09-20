import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
f = int(input())

print(a.count(f))