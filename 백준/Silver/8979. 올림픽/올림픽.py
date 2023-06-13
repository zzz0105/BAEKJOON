N, K = map(int,input().split())
medals = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x:(-x[1],-x[2],-x[3]))
K_medal = ()
for medal in medals:
    if medal[0] == K:
        K_medal = medal[1:]
for i in range(N):
    if medals[i][1:] == K_medal:
        print(i+1)
        break