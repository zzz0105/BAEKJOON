def solution(survey, choices):
    answer = ''
    scores = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            scores[survey[i][0]] += 4 - choices[i] 
        elif choices[i] > 4:
            scores[survey[i][1]] += choices[i] - 4
            
    scores = tuple(scores.items())
    for i in range(4):
        type1, score1 = scores[2*i]
        type2, score2 = scores[2*i+1]
        answer += type1 if score1>=score2 else type2
        
    return answer