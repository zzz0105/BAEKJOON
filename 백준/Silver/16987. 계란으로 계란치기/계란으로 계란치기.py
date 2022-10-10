import sys

def check(eggs):
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def break_egg(idx, eggs):
    global cnt, n
    if idx == n:
        cnt = max(cnt, check(eggs))
        return
    if eggs[idx][0] <= 0:
        break_egg(idx+1, eggs)
    else:
        all_broken = True
        for i in range(n):
            if idx != i and eggs[i][0] > 0:
                all_broken = False
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                break_egg(idx+1, eggs)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
        if all_broken:
            break_egg(idx+1, eggs)
    
n = int(sys.stdin.readline().rstrip())
eggs = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
cnt = 0
break_egg(0, eggs)
print(cnt)