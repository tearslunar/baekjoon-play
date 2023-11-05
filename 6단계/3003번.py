sn = list(map(int, input().split()))
nn = [1, 1, 2, 2, 2, 8]
for i in range(len(sn)):
    nn[i] = nn[i] - sn[i]
nn_1 = ' '.join(str(s) for s in nn)
print(nn_1)