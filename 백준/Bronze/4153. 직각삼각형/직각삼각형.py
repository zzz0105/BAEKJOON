while True:
    a = sorted(list(map(int,input().split())))
    if a == [0,0,0]: break
    print('right' if a[2]*a[2] == a[1]*a[1] + a[0]*a[0] else 'wrong')