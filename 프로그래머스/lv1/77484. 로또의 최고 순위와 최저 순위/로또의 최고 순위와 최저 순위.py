def solution(lottos, win_nums):
    # 최소 1등, 최대 6등
    lowest_rank = min(7-len(set(lottos)&set(win_nums)),6)
    return [max(lowest_rank-lottos.count(0),1), lowest_rank]