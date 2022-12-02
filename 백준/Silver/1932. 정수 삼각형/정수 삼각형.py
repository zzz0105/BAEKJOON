n = int(input())
tri = [list(map(int,input().split())) for _ in range(n)]
for h in range(1,n):
    for i in range(len(tri[h])):
        if i == 0:
            tri[h][i] += tri[h-1][i]
        elif i == len(tri[h])-1:
            tri[h][i] += tri[h-1][-1]
        else:
            tri[h][i] += max(tri[h-1][i-1], tri[h-1][i])
print(max(tri[-1]))