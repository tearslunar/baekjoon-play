n  = int(input())
a = list(map(int, input().split()))
min = a[0]
max = a[0]
for i in range(n):
    if a[i] <= min:
        min = a[i]
    elif a[i] >= max:
        max = a[i]
        
print(min, max,end=' ')