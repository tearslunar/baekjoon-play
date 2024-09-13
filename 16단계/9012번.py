import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    vps = input().rstrip()
    for i in vps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")