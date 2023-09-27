n = int(input())
answer = []
score = list(map(int, input().split()))
for i in range(n):
    new = score[i]/max(score)*100
    answer.append(new)
    
arg = sum(answer)/n
print(arg)