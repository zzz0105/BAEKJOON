import sys
input = sys.stdin.readline

def check(arr):
    global friends
    if len(arr) == 5:
        print(1)
        exit(0)
    for friend in friends[arr[-1]]:
        if friend not in arr:
            check(arr+[friend])

N, M = map(int,input().split())
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
for i in range(N):
    check([i])
print(0)