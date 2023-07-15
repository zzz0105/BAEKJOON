def solution(numbers, hand):
    answer = ''
    l, r = '*', '#'; # 왼손과 오른손의 현재 위치
    position = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}
    for number in numbers:
        if number in {1,4,7}:
            l = number
            answer += 'L'
        elif number in {3,6,9}:
            r = number
            answer += 'R'
        else:
            l_dist = abs(position[l][0]-position[number][0]) + abs(position[l][1]-position[number][1])
            r_dist = abs(position[r][0]-position[number][0]) + abs(position[r][1]-position[number][1])
            if l_dist<r_dist or (l_dist==r_dist and hand=='left'):
                l = number
                answer += 'L'
            elif l_dist>r_dist or (l_dist==r_dist and hand=='right'):
                r = number
                answer += 'R'
    return answer