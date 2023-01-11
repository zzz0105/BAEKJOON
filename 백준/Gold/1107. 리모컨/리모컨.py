N = int(input())    #최종 목표 채널
M = int(input())
broken = set(input().split()) if M else set()
min_cnt = abs(N-100)    
# 현재 채널(100)에서 N까지 +나 -로만 이동한 최소 횟수

for ch in range(1000000):
    ch = str(ch)
    make_possible = True    # 고장나지 않은 버튼들로 채널을 만들 수 있는지
    for i in range(len(ch)):
        if ch[i] in broken:
            make_possible = False
            break
    if make_possible:
        min_cnt = min(min_cnt, len(ch)+abs(N-int(ch)))
        # 채널 버튼 누르는 횟수 + 그 채널에서 N까지 +나 -로만 이동한 최소 횟수

print(min_cnt)