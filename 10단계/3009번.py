for _ in range(3):
    x, y = map(int, input().split())
    x.append(x)
    y.append(y)

vx = 0
vy = 0
for i in range(len(x)):
    if x.count(x[i]) == 1:
        vx = x[i]
for i in range(len(y)):
    if y.count(y[i]) == 1:
        vy = y[i]
        
print(vx, vy)