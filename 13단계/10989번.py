import sys #계수정렬

n = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(n):
    count[int(input())] += 1

for i in range(len(count)):
    if count[i] !=0:
        for _ in range(count[i]):
            print(i)