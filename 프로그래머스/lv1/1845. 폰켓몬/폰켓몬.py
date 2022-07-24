from collections import Counter
def solution(nums):
    n = Counter(nums)
    max_p = len(nums)//2
    return min(max_p, len(n))