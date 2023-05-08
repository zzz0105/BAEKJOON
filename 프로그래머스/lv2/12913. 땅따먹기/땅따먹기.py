def solution(land):
    answer = 0

    N = len(land)
    for r in range(1,N):
        for bc in range(4):
            max_score = 0
            for nc in range(4):
                if bc!=nc:
                    max_score = max(max_score, land[r-1][nc])
            land[r][bc] += max_score

    return max(land[-1])