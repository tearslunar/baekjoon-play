stick = list(map(int, input().split()))
if max(stick) >= sum(stick) - max(stick):
        stick[stick.index(max(stick))] = sum(stick) - max(stick) - 1
        print(sum(stick))
else:
    print(sum(stick))

    
#다른방법
# stick = sorted(map(int, input().split()))
# a = stick[0] + stick[1] + min(li[2], li[0]+li[1]-1)
# print(a)