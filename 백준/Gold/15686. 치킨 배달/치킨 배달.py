import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def choose(c):
    global N, M, chickens
    if len(c)==M:
        cal(c)
    j = 0 if len(c)==0 else chickens.index(c[-1])
    for i in range(j, len(chickens)):
        if chickens[i] not in c:
            c.append(chickens[i])
            choose(c)
            c.pop()

def cal(ch):
    global houses, answer
    total_cd = 0
    for h in houses:
        cd = float('inf')
        for c in ch:
            cd = min(cd, abs(c[0]-h[0])+abs(c[1]-h[1]))
        total_cd += cd
    answer = min(answer, total_cd)

N, M = map(int,input().split())
houses = []
chickens = []
answer = float('inf')
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] == 1:
            houses.append((i,j))
        elif tmp[j] == 2:
            chickens.append((i,j))
choose([])
print(answer)