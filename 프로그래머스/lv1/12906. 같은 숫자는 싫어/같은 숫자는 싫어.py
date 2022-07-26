def solution(arr):
    answer = []
    while arr:
        a = arr.pop()
        for _ in range(len(arr)):
            r = arr.pop()
            if a != r:
                arr.append(r)
                answer.append(a)
                break 
    answer.append(a)
    answer.reverse()
    return answer