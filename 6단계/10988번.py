word = input()
a = round(len(word)/2)
b = 0
for i in range(a):
    if word[i] == word[(-1*i)-1]:
        b = b + 1
if b == a:
    print('1')
else:
    print('0')