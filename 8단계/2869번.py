a, b, v = map(int, input().split())

now = 0
day = 0
distance = v - b
move = a - b

if distance % move == 0:
    day = distance // move
else:
    day = distance // move + 1

print(day)