import sys

def cnt_eat(candies):
    global max_candy, n
    for i in range(n):
        tmp = 1
        for j in range(1,n):
            if candies[i][j] == candies[i][j-1]:
                tmp += 1
                max_candy = max(max_candy, tmp)
            else:
                tmp = 1
        tmp = 1
        for j in range(1, n):
            if candies[j][i] == candies[j-1][i]:
                tmp += 1
                max_candy = max(max_candy, tmp)
            else:
                tmp = 1

n = int(sys.stdin.readline().rstrip())
candies = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
move = [(1,0), (0, 1), (-1,0), (0,-1)]
max_candy = 0
for i in range(n):
    for j in range(n):
        for di, dj in move:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and candies[i][j]!=candies[ni][nj]:
                candies[ni][nj], candies[i][j] = candies[i][j], candies[ni][nj]
                cnt_eat(candies)
                candies[ni][nj], candies[i][j] = candies[i][j], candies[ni][nj]

print(max_candy)