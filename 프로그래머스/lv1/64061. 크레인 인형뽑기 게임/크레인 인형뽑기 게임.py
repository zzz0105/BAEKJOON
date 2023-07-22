def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for i in range(len(board)):
            picked = board[i][move-1]
            board[i][move-1] = 0
            if picked!=0:
                if basket and basket[-1]==picked:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(picked)
                break
    return answer