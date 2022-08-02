def solution(citations):
    answer = len(citations)
    citations.sort()
    while True:
        cnt = 0
        for citation in citations:
            if citation >= answer:
                cnt += 1
            if answer <= cnt:
                return answer
        answer -= 1        
    return answer