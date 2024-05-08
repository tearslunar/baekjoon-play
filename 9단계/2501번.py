a, b = map(int, input().split())
measure = []

for i in range(1, a+1):
    if a % i == 0:
        measure.append(i)

if len(measure) >= b:
    print(measure[b-1])
else:
    print(0)
    
# 다른방법 raise 예외발생 사용해도 되고 안해도 됨
# try:
#     print(measure[b-1])
# except:
#     print("0")