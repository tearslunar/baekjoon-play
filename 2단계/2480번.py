a, b, c = map(int, input().split())
if a == b == c:
    print(10000+(a*1000))
elif a == b or b == c or c == a:
    if a == b:
        print(1000+(a*100))
    elif b == c:
        print(1000+(b*100))
    elif a == c:
        print(1000+(a*100))
else:
    if a > b and a > c:
        print(a*100)
    elif b > c and b > a:
        print(b*100)
    elif c > a and c > b:
        print(c*100)