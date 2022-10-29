import sys

def choose(start):
    global ans, n
    if len(start)==n//2:
        a,b = 0,0
        link = list(set(range(n)) - set(start))
        for x in range(n//2):
            for y in range(x+1, n//2):
                a += powers[start[x]][start[y]] + powers[start[y]][start[x]]
                b += powers[link[x]][link[y]] + powers[link[y]][link[x]]
        ans = min(ans, abs(a-b))
        return
    j = 0 if len(start)==0 else start[-1]+1
    for i in range(j, n):
        start.append(i)
        choose(start)
        start.pop()

n = int(sys.stdin.readline().rstrip())
powers_sum = 0
powers = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
ans = float('inf')
choose([])
print(ans)