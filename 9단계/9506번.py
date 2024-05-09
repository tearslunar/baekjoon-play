while True:
    a = int(input())

    if a == -1:
        break
    
    meansure = []
    for i in range(1, a+1):
        if a % i == 0:
            meansure.append(i)
    meansure.remove(a)

    if sum(meansure) == a:
        print("{0} = ".format(a), end='')
        print(*meansure, sep=' + ')
    else:
        print("{0} is NOT perfect.".format(a))