for _ in range(int(input())):
    H, W, N = map(int,input().split())
    N-=1
    print((N%H+1)*100+N//H+1)