while True:
    a, b = map(int, input().split())
    
    if a == 0 == b:
        break
    
    c = False
    d = False

    if b % a == 0:
        c = True
    elif a % b == 0:
        d = True

    if c:
        print("factor")
    elif d:
        print("multiple")
    else:
        print("neither")