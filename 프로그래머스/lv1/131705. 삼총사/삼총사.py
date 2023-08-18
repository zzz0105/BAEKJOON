from itertools import combinations

def solution(number):
    return sum([sum(c)==0 for c in combinations(number,3)])