a = int(input())
b = [input().split() for _ in range(int(a))]
c = [[0 for _ in range(100)] for _ in range(100)]
extent = 100*a

for k in range(a):
    for i in range(10):
        for j in range(10):
            if c[i+(89-int(b[k][1]))][j+(89-int(b[k][0]))] == 0:
                c[i+(89-int(b[k][1]))][j+(89-int(b[k][0]))] = 1
            elif c[i+(89-int(b[k][1]))][j+(89-int(b[k][0]))] == 1:
                extent = extent - 1
                
print(extent)