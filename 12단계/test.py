n = int(input())
kg5 =  n // 5
kg3 = (n % 5) // 3
print(kg5, kg3)
m = n - ((kg3 * 3) + (kg5 * 5))
print(m)