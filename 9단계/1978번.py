n = int(input())
num = list(map(int, input().split()))
count = 0

for i in num:
    for k in range(2, i+1):
        if i % k == 0:
            if i == k:
                count += 1
            break
print(count)

# 다른방법
n = int(input())
num = list(map(int, input().split()))
prime = []

for i in num:
    ju = True
    if i == 1:
        ju = False
    for k in range(2, i):
        if i % k == 0:
            ju = False

    if ju:
        prime.append(i)
print(len(prime))
