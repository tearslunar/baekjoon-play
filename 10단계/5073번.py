while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    d = [ a, b, c]
    if max(d) >= sum(d)-max(d) or d.count(0) >= 1:
        print("Invalid")
    elif len(set(d)) == 1:
        print("Equilateral")
    elif len(set(d)) == 2:
        print("Isosceles")
    elif len(set(d)) == 3:
        print("Scalene")