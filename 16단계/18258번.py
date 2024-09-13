import sys
from collections import deque
input = sys.stdin.readline
que = []
deque = deque(que)
n = int(input())
for i in range(n):
    a = input().rstrip()
    
    if "push" in a:
        b = a.split()
        deque.append(int(b[1]))
    elif a == "pop":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif a == "size":
        print(len(deque))
    elif a == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif a == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif a == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)