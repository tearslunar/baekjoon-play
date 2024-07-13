n, m = map(int, input().split())
chess = []
result = []
for i in  range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7):
        ws = 0
        bs = 0
        for h in range(i, i+8):
            for w in range(j, j+8):
                if (h+w) % 2 == 0: #처음 시작을 분류
                    if chess[h][w] != 'W': #처음시작이 W
                        ws += 1            #처음시작이 W일때의 경우의 수
                    if chess[h][w] != 'B': #처음시작이 B
                        bs += 1            #처음시작이 B일때의 경우의 수
                else:                      #자동으로 뒤따라 오는것들
                    if chess[h][w] != 'B': #대응
                        ws += 1
                    if chess[h][w] != 'W': #대응
                        bs += 1
        result.append(min(ws, bs))
    
print(min(result))