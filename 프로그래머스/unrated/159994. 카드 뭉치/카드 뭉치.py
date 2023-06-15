def solution(cards1, cards2, goal):
    answer = 'Yes'
    idx_1, idx_2, idx_goal = 0, 0, 0
    
    while True:
        if idx_goal == len(goal):
            break
        if idx_1 < len(cards1) and goal[idx_goal] == cards1[idx_1]:
            idx_1 += 1
            idx_goal += 1
        elif idx_2 < len(cards2) and goal[idx_goal] == cards2[idx_2]:
            idx_2 += 1
            idx_goal += 1
        else:
            answer = 'No'
            break
        
    return answer