def solution(clothes):
    closet = {}
    answer = 1
    for c in clothes:
        closet[c[1]] = closet.get(c[1], 0) + 1
    for c in closet:
        answer *= (1+closet[c])
    return answer - 1