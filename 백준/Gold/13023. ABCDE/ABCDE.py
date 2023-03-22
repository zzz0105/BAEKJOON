import sys
input = sys.stdin.readline

def check(arr):
    global friends, visited
    if len(arr) == 5:
        print(1)
        exit(0)
    for friend in friends[arr[-1]]:
        if not visited[friend]:
            visited[friend] = True
            check(arr+[friend])
            visited[friend] = False

N, M = map(int,input().split())
friends = [[] for _ in range(N)]
visited = [False]*N
for _ in range(M):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
for i in range(N):
    visited[i] = True
    check([i])
    visited[i] = False
print(0)