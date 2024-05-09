min1 = int(input())
max1 = int(input())
prime = []
for i in range(min1, max1+1):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                prime.append(i)
            
            break
if len(prime) != 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)