rating = ["A+","A0","B+","B0","C+","C0","D+","D0","F"]
score = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]

sum1 = 0
sum2 = 0

for i in range(20):
    a, b, c = input().split()
    if c == 'P':
        continue
    else:
        sum1 += float(b)
        sum2 += float(b)*float(score[rating.index(c)])
        
print( '%.6f'%(sum2/sum1))