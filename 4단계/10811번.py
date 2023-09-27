m, n = map(int, input().split())

answer = list(i+1 for i in range(m))

for i in range(n):
    a, b = map(int, input().split())
    answer[a-1:b] = reversed(answer[a-1:b])

for i in range(m):
    print(answer[i], end=' ')
    
#다음부터는 모든거 다쓰기 괜히 객기부리고 지랄하지 말기 ㅇㅋ?