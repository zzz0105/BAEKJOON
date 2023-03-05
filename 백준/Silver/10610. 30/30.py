N = sorted(list(map(int, list(input()))), reverse=True)
if sum(N)%3==0 and N[-1]==0:
    print(*N, sep='')
else:
    print(-1)