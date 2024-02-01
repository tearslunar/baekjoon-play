arr = [list(map(int, input().split())) for _ in range(9)]
maxl = []
iy = []
ix = []
for i in range(9):
    maxl.append((max(arr[i])))
    ix.append(arr[i].index(max(arr[i])))
    iy.append(i)
print(max(maxl))
print(iy[maxl.index(max(maxl))]+1, ix[maxl.index(max(maxl))]+1)