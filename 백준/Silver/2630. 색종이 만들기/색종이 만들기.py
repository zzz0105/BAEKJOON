import sys

def sol(x, y, size):
    global papers, white, blue
    color = papers[x][y]
    for i in range(size):
        for j in range(size):
            if papers[x+i][y+j] != color:   #지정된 크기 안에서 색이 다르면 쪼갠다.
                size //= 2
                sol(x, y, size)
                sol(x+size, y, size)
                sol(x, y+size, size)
                sol(x+size, y+size, size)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

n = int(sys.stdin.readline())
papers = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
white, blue = 0, 0
sol(0, 0, n)
print(white)
print(blue)