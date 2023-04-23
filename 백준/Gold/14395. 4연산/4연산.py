from collections import deque

S, T = map(int, input().split()) 
q = deque([(S,'')])
visited = {S}
is_possible = False
while q:
    now, ops = q.popleft()
    if now == T:
        is_possible = True
        break
    sn = str(now)
    for o in ('*','+','-','/'):
        if not now and o=='/':
            continue
        res = eval(sn+o+sn)
        if res <= T and res not in visited:
            # res>T일 때 +,*:res 더 커짐 -,/:연산결과가 각 0과 1로, 최소연산아님. 따라서 res>T일 때는 고려x 
            visited.add(res)
            q.append((res, ops+o))

print(-1 if not is_possible else (ops if S!=T else 0))