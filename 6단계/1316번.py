c = int(input())
a = False
for _ in range(c):
    a = False
    word = input()
    word1 = list(set(word))
    for j in word1:
        if a == True:
            break
        if word.count(j) > 1:
            A = word.find(j)
            B = word.rfind(j)
            for i in range(A, B+1):
                if j == word[i]:
                    pass
                else:
                    c -= 1
                    a = True
                    break
        else:
            pass              
print(c)