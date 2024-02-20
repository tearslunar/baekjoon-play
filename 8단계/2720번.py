case = int(input())

for i in range(case):
    change = int(input())
    
    q = change // 25
    change -= q*25
    d = change // 10
    change -= d*10
    n = change // 5
    change -= n*5

    print(q, d, n, change)