for _ in range(int(input())):
    H, W, N = map(int,input().split())
    print(N%H*100+N//H+1 if N%H else H*100+N//H)