b = 0                                   #처음
answer = [] 
for i in range(28):
    try:
        a = int(input())
        b = i+1
        if a != b:
            for i in range(a-b-1, a-b+1):
                answer.append(i)
    except:
        answer.append(29)
        answer.append(30)
        
for i in range(0, 2):
    print(answer[i])

                                    #나중
a = [i for i in range(1,31)]

for _ in range(28):
    b = int(input())
    a.remove(b)

print(min(a))
print(max(a))