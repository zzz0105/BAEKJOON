from collections import deque
import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
connect = {}
hacked_result = {}
for _ in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    connect[b] = connect.get(b, []) + [a]
believed_com = connect.keys()
for start in believed_com:
    q = deque()
    visited = [0]*(n+1)
    hacked = 0
    visited[start] = True    
    q.append(start)
    while q:
        start_com = q.popleft()
        if start_com in believed_com:
            for hacked_com in connect[start_com]:
                if not visited[hacked_com]:
                    q.append(hacked_com)
                    visited[hacked_com] = 1
    hacked_result[start] = sum(visited)
hacked_result = sorted(hacked_result.items(), key= lambda x:(-x[1],x[0]))
maxi = hacked_result[0][1]
for com, hacked in hacked_result:
    if hacked == maxi:
        print(com, end=' ')
    else:
        break