from collections import deque

N = int(input())
M = int(input())
friends = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int,input().split())
  friends[a].append(b)
  friends[b].append(a)

invited = set([1])
q = deque([(1, 0)])
while q:
  i, cnt = q.popleft()
  for j in friends[i]:
    if j not in invited and cnt<2:
      q.append((j, cnt+1))
      invited.add(j)
      
print(len(invited)-1)