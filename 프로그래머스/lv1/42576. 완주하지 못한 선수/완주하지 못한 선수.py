def solution(participants, completions):
    participants.sort()
    completions.sort()
    flag = 0
    for i in range(len(completions)):
        if participants[i]!=completions[i]:
            flag = 1
            break
    if flag==0:
        return participants[-1]
    else:
        return participants[i]