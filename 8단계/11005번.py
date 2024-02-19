a, b = map(int, input().split())
c = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = ''

while a != 0:
    d += str(c[a%b])
    a //= b
   
print(d[::-1])