nl = []

for _ in range(5):
    a = input()
    nl.append(list(a))

maxlen = 0

for i in range(5):
    if maxlen > len(nl[i]):
        pass
    else:
        maxlen = len(nl[i])

for i in range(maxlen):
    for j in range(5):
        if len(nl[j]) < i+1:
            continue
        else:
            print(nl[j][i], end='')

    
'''
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''