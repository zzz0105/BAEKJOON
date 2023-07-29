def find(c):        # 부모 찾기
    if parent[c]==c:
        return c
    return find(parent[c])

def union(c1,c2):   # 집합 합치기
    c1 = find(c1)
    c2 = find(c2)
    if c1!=c2:
        parent[max(c1,c2)] = min(c1,c2)

N = int(input())    # 컴퓨터 수
M = int(input())    # 컴퓨터 쌍의 수

parent = [i for i in range(N+1)]

for i in range(M):
    c1, c2 = map(int,input().split())
    union(c1,c2)

answer = 0
for i in range(2,N+1):
    if find(i) == parent[1]:
        answer += 1
print(answer)