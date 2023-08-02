def solution(n, s):     # 원소 개수 n, 원소의 합 s
    return [s//n]*(n-s%n) + [s//n+1]*(s%n) if n<=s else [-1]