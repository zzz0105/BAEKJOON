from collections import Counter

def solution(k, tangerine):
    tangerine_cnt = sorted(Counter(tangerine).items(), key=lambda x:-x[1])
    # (크기, 개수)      개수 순으로 정렬
    remove = len(tangerine) - k 
    while remove:
        size, ea = tangerine_cnt.pop()
        if remove >= ea:
            remove -= ea
        else:
            tangerine_cnt.append((size, ea-remove))
            break
    return len(tangerine_cnt)