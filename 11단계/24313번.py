a1 , a2 = map(int, input().split())
c = int(input())
n = int(input())

if (a1 * n) + a2 <= (n * c) and a1 <= c: #a1 이 -일때
    print(1) 
else:
    print(0)
    