N = int(input())
tower = tuple(map(int,input().split()))
answer = [0]*N
stack = []

for i in range(N-1,-1,-1):
    while stack and tower[i] > tower[stack[-1]]:
        j = stack.pop()
        answer[j] = i+1
    stack.append(i)

print(*answer, sep=' ')