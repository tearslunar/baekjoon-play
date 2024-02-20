n = int(input())
m = 2
a = 1
for i in range(n):
    m += a
    a *= 2
    
print(m**2)