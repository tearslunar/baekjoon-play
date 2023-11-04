sum = 0
string = input()
for i in range(len(string)):
    if 65 <= ord(string[i]) <= 67: #ABC
        sum += 3
    elif 68 <= ord(string[i]) <= 70: #DEF
        sum += 4
    elif 71 <= ord(string[i]) <= 73: #GHI
        sum += 5
    elif 74 <= ord(string[i]) <= 76: #JKL
        sum += 6
    elif 77 <= ord(string[i]) <= 79: #MNO
        sum += 7
    elif 80 <= ord(string[i]) <= 83: #PQRS
        sum += 8
    elif 84 <= ord(string[i]) <= 86: #TUV
        sum += 9
    elif 87 <= ord(string[i]) <= 90: #WXYZ
        sum += 10
print(sum)
#노가다

#for문
li = ["ABC" , "DEF" , "GHI" , "~~"]
for i in string:
    for j in li:
        if i in j:
            sum1 = li.index(j) + 3
            
li = ["ABC" , "DEF" , "GHI" , "~~"]
for i in string:
    for j in range(len(li)):  
        if i in li[j]:  # j 안에 i가 있는지 O i안에 j가 있는지 X
            sum1 = j + 3 #변형 버전