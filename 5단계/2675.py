loof = int(input())

for i in range(loof):
    lf, st = input().split()
    for j in range(len(st)):
        print(st[j]*int(lf), end='')
    print()