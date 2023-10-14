from collections import deque
from pprint import pprint


def bfs(r, c, k):
    dq = deque()
    dq.append((r, c, k))
    visited = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[r][c][k] = 0
    while dq:
        r, c, k = dq.popleft()
        if r == H - 1 and c == W - 1:
            return visited[r][c][k]
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc][k] == -1 and arr[nr][nc] == '0':
                dq.append((nr, nc, k))
                visited[nr][nc][k] = visited[r][c][k] + 1
        for dr, dc in ((-1, 2), (1, 2), (2, -1), (2, 1), (1, -2), (-1, -2), (-2, 1), (-2, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and k < K and visited[nr][nc][k + 1] == -1 and arr[nr][nc] == '0':
                dq.append((nr, nc, k + 1))
                visited[nr][nc][k + 1] = visited[r][c][k] + 1
    return -1


K = int(input())
W, H = map(int, input().split())
arr = tuple(tuple(input().split()) for _ in range(H))
print(bfs(0, 0, 0))
