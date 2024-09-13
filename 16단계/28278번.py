import sys
input = sys.stdin.readline

class stack:
    def __init__(self):
        self.stlist = []

    def push(self, x):
        self.stlist.append(x)

    def out(self):
        self.stlist.pop()

st = stack()
n = int(input())
for i in range(n):
    commend = int(input())
    
    if commend == 0:
        st.out()
    else:
        st.push(commend)
        
print(sum(st.stlist))
