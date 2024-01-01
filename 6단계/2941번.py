word = input()
print(word)
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

sum = len(word)

for i in croatia:
    
    if i in word:
        sum -= word.count(i)

print(sum)