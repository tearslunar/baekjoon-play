x = int(input())
y = 0

z = 0
den = 0
mol = 0

while x > 0:
	y += 1
	x -= y

z = y
x = y + x - 1


if z % 2 == 0:
	den = y
	mol = 1
	for _ in range(1, x+1):
		den -= 1
		mol += 1
else:
	mol = y
	den = 1
	for _ in range(1, x+1):
		den += 1
		mol -= 1

print("{0}/{1}".format(mol, den))