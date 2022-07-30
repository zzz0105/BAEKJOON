def solution(sizes):
    sizes = list(zip(*map(sorted, sizes)))    
    return max(sizes[0]) * max(sizes[1])