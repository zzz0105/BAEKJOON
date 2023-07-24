from collections import Counter

def solution(X, Y):
    answer = ''
    x, y = Counter(X), Counter(Y)
    for num in sorted(x.keys(), reverse=True):
        if num in y.keys():
            answer += num*min(x[num], y[num])
    if answer: return "0" if answer[0]=="0" else answer
    else:   return "-1"