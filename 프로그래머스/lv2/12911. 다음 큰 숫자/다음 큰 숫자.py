def solution(n):
    n_one = str(bin(n)).count('1')
    for num in range(n+1,1000001):
        if str(bin(num)).count('1') == n_one:
            return num