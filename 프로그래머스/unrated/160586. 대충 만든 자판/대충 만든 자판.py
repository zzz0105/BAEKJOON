def solution(keymap, targets):
    answer = [0]*len(targets)
    time = {}
    
    for km in keymap:
        for i in range(len(km)):
            key = km[i]
            if key not in time.keys():
                time[key] = i+1
            else:
                time[key] = min(i+1, time[key])
                
    for i in range(len(targets)):
        for j in range(len(targets[i])):
            if targets[i][j] in time.keys() and answer[i]!=-1:
            # 목표 문자 작성 가능하며 이전의 목표 문자들도 작성할 수 있을 때
                answer[i] += time[targets[i][j]]
            else:
                answer[i] = -1  # 작성 불가
        
    return answer