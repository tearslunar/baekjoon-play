word = input()
result = [ ]
abcd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#set(word) 를 사용해서 중복제거하고 저장가능

word = word.lower()

for i in abcd:
    a = 0
    for j in range(len(word)):
        if word[j] == i:
            a = a + 1            
    result.append(a)


max_sum = 0

for i in result:
    if i == max(result):
        max_sum = max_sum + 1
        
    
if max_sum > 1:
    print("?")

else:
    print(abcd[result.index(max(result))].upper())