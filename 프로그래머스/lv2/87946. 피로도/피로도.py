from itertools import permutations 
def solution(k, dungeons):
    answer = 0
    d = len(dungeons)
    orders = list(permutations(range(d), d))
    for order in orders:
        f = k
        a = 0
        for o in order:
            if f < dungeons[o][0]:
                continue
            f -= dungeons[o][1]
            a += 1
        answer = max(a, answer)
    return answer