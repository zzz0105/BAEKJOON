import sys
input = sys.stdin.readline

N, S = map(int,input().split())
nums = map(int,input().split())

cs = [0]        #누적합
for num in nums:
    cs.append(cs[-1]+num)

answer = float('inf')
l, r = 0, 1     #투포인터
while l != N:
    if cs[r] - cs[l] >= S:
        answer = min(r-l, answer)
        l += 1
    else:
        if r != N:
            r += 1
        else:
            l += 1
print(0 if answer==float('inf') else answer)