def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a1, a2 = arr1[i],arr2[i]
        row = ""
        for _ in range(n):
            if (a1%2)|(a2%2):   row = "#" + row
            else:   row = " " + row
            a1, a2 = a1//2, a2//2 
        answer.append(row)
        
    return answer