def solution(n):
    answer, s, e, sum_se = 0, 1, 1, 1  # sum_se: s부터 e까지의 합
    
    while s<=e:
        if sum_se == n:
            answer += 1
            
        if sum_se >= n:
            sum_se -= s
            s += 1
        else:
            e += 1
            sum_se += e
            
    return answer