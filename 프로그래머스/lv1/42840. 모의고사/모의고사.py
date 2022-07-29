def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1,c2,c3 = 0,0,0
    
    for i in range(len(answers)):
        if answers[i] == p1[i%5]:
            c1 += 1
        if answers[i] == p2[i%8]:
            c2 += 1
        if answers[i] == p3[i%10]:
            c3 += 1        
            
    c = [c1,c2,c3]
    m = max(c)
    
    for i in range(len(c)):
        if c[i]==m:
            answer.append(i+1)
            
    return answer