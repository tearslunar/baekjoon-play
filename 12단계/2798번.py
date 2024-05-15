n , m = map(int, input().split())
card = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in rnage(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                sum  = max(sum, card[i] + card[j] + card[k])
print(sum)

#for문 선택