N = int(input())
A = tuple(map(int,input().split()))
stack = []
answer = [-1]*N
for i in range(N):
    while stack and A[stack[-1]]<A[i]:
        j = stack.pop()
        answer[j] = A[i]
    stack.append(i)
print(*answer)