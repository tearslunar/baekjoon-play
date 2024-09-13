import sys
input = sys.stdin.readline

while True:
    stack = []
    n = input().rstrip()
    if n == ".":
        break
        
    for i in n:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack:
                if stack.pop() == "(":
                    continue
                else:
                    print('no')
                    break
            else:
                print("no")
                break
        elif i == "]":
            if stack:
                if stack.pop() == "[":
                    continue
                else:
                    print('no')
                    break
            else:
                print("no")
                break
    else:
        if not stack:
            print("yes")
        else:
            print("no")
