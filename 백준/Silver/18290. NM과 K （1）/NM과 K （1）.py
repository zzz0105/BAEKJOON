import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def choose(selected, selected_sum):
    global arr, answer, visited, N, M, K
    if len(selected)==K:
        answer = max(answer, selected_sum)
        return
    bi = selected[-1][0] if selected else 0
    bj = selected[-1][1] if selected else 0
    for i in range(bi,N):
        for j in range(bj if i==bi else 0,M):
            if visited[i][j]: continue
            for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=ni<N and 0<=nj<M and visited[ni][nj]:
                    break
            else:   
                selected.append((i,j))
                visited[i][j] = True
                selected_sum += arr[i][j]
                choose(selected, selected_sum)
                selected.pop()
                visited[i][j] = False
                selected_sum -= arr[i][j]

N, M, K = map(int, input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]
answer = float('-inf')
visited = [[False]*M for _ in range(N)]
choose([],0)
print(answer)