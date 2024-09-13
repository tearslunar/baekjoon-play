import sys
from collections import deque
input = sys.stdin.readline
deq = deque()
n = int(input())
for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        deq.appendleft(command[1])
    if command[0] == 2:
        deq.append(command[1])
    if command[0] == 3:
        print(deq.popleft() if deq else -1)
    if command[0] == 4:
        print(deq.pop() if deq else -1)
    if command[0] == 5:
        print(len(deq))
    if command[0] == 6:
        print(0 if deq else 1)
    if command[0] == 7:
        print(deq[0] if deq else -1)
    if command[0] == 8:
        print(deq[-1] if deq else -1)
        

    
    
