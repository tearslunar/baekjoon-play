import sys
input = sys.stdin.readline

n = int(input())
qu = list(map(int, input().split()))
stack = []
last = 1

def st():
    global last
    if stack and stack[-1] == last:
        last += 1
        stack.pop()
        st()

for i in qu:
    if i == last:
        last += 1
    else:
        stack.append(i)
    st()

if not stack:
    print("Nice")
else:
    print("Sad")