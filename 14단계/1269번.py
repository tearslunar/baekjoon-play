import sys
input = sys.stdin.readline
n, m = map(int ,input().split())
li = set(input().split())
ul = set(input().split())

print( len(li ^ ul))