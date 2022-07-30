from itertools import permutations

def isPrime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    pers, ns = [], []
    for i in range(1,len(numbers)+1):
        pers.extend(list(permutations(numbers, i)))
    ns.extend(list(map(int, map(''.join, pers))))
    for n in list(set(ns)):
        answer += isPrime(n)
    return answer