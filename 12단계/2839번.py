n = int(input())
kg5 =  n // 5
kg3 = (n % 5) // 3
result = []
while(True):
    if kg3 * 3 + kg5 * 5 == n:
        result.append(kg5 + kg3)
        if kg5 == 0:
            break
        kg5 -= 1
        kg3 = (kg3 * 3 + 5) // 3
    else:
        if kg5 == 0:
            break
        m = n - ((kg3 * 3) + (kg5 * 5))
        kg5 -= 1
        kg3 = (kg3 * 3 + 5 + m) // 3
        continue

if len(result) != 0:
    print(min(result))
else:
    print('-1')

#while 사용
#for문도 사용가능
#for i in range(N//5+1) 사용해서 5kg이 0일때부터 시작해서 최솟값을 answer변수에 저장한다
#i가 0일때 3으로 나누어 떨어지면 answer에 그 값을 저장한다.
#m에다가 원래 kg에서 5*i만큼 빼서 차이값을 저장한다.
#m을 3으로 나누고 나누어떨어지면 min을 활용해서 answer에 i + m//3 과 기존에 있던 answer값을 비교해서 작은값을 저장한다.

#answer의 값은 나우어떨어지지 않으면 저장되지 않게 만들어졌기 떄문에 처음에 설정한 값인 0이 그대로 유지된다면 마지막에 if문으로 -1을 출력하고
#아니라면 answer을 출력한다.