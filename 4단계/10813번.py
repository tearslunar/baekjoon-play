m, n = map(int, input().split())
x = []

for i in range(m):
    x.append(i+1)
    
for i in range(n):
    a, b = map(int, input().split())
    c = x[b-1]
    x[b-1] = x[a-1]
    x[a-1] = c

    
for i in range(m):
    print(x[i], end=' ')
    
#for _ in range() 변수값 없이 반복문 작동 다음부터 써볼것