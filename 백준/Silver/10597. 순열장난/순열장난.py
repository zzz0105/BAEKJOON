import sys
sys.setrecursionlimit(10**6)

def restore(idx, order):
    global visited
    if idx == length and order == max_num:
        print(*answer, sep=' ')
        sys.exit(0)

    num = int(N[idx])                   # 한자리수일 때
    if num > 0 and not visited[num]:
        visited[num] = True
        answer[order] = num
        restore(idx+1, order+1)
        visited[num] = False
    if idx < len(N)-1:                  # 두자리수일 때
        num = int(N[idx]+N[idx+1])
        if num <= max_num and not visited[num]:
            visited[num] = True
            answer[order] = num
            restore(idx+2, order+1)
            visited[num] = False

N = input()
length = len(N)
max_num = length if length<=9 else 9 + (length-9)//2    # 수열에서 가장 큰 수
answer = [0]*(max_num)          # i번째로 방문한 숫자
visited = [False]*(max_num+1)   # 숫자 i 방문 여부
restore(0, 0)