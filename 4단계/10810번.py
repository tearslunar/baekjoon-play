n,m = map(int, input().split())

basket = [0]*n

for l in range(m):
  i,j,k = map(int,input().split())
  for x in range(i,j+1):      #중요
    basket[x-1] = k

for x in range(n):
  print(basket[x], end=" ")
  라ㅓㅁㄴ