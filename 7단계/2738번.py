N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
sum = [[0 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for i in range(N):
        sum[i][j] = arr1[i][j] + arr2[i][j]
    
for i in range(N):
    for j in range(M):
        print(sum[i][j], end=' ')
    print()