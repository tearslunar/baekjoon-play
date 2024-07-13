li = []
for i in range(5):
    a = int(input())
    li.append(a)

print(sum(li) // 5)
li.sort()
print(li[2])