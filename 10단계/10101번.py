angle = []
for _ in range(3):
    angle.append(int(input()))
angled = angle.copy()
angle = set(angle)

if sum(angled) == 180:
    if len(angle) == 1:
        print("Equilateral")
    elif len(angle) == 2:
        print("Isosceles")
    elif len(angle) == 3:
        print("Scalene")
else:
    print("Error")