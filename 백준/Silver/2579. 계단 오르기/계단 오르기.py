# 마지막 계단은 꼭 밟아야 함 -> 직전 계단을 밟음/밟지 않음 경우로 나눠 생각하기
# 직전 계단을 밟음 -> 연속 세 개 밟지 못하므로 2칸 - 1칸 올라옴
# 직전 계단을 밟지 않음 -> 한 번에 2칸 올라옴
n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
scores = [0]*(n+1)  # i번째 stairs 올라오기 최대 점수
scores[1] = stairs[1]   
if n > 1:   #IndexError 주의
    scores[2] = stairs[1] + stairs[2]
    for i in range(3, n+1):
        scores[i] += max(scores[i-3] + stairs[i-1], scores[i-2]) + stairs[i]
print(scores[n])