n = int(input())
vx = []
vy = []
for i in range(n):
    x, y = map(int , input().split())
    vx.append(x)
    vy.append(y)
    
print((max(vx)-min(vx))*(max(vy)-min(vy)))