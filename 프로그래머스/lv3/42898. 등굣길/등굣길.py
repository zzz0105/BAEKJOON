def solution(m, n, puddles):
    road = [[1]*(m+1) for _ in range(n+1)]
    for pc, pr in puddles:
        road[pr][pc] = 0
        # 최단경로는 1행 혹은 1열에 위치한 물에 잠긴 지역 뒤를 거치지 않는다
        if pc == 1:
            for r in range(pr+1,n+1):
                road[r][pc] = 0
        elif pr == 1:
            for c in range(pc+1,m+1):
                road[pr][c] = 0
        
    for i in range(2,n+1):
        for j in range(2,m+1):
            if road[i][j] == 0:  continue
            if road[i-1][j] == 0:
                road[i][j] = road[i][j-1]
            elif road[i][j-1] == 0:
                road[i][j] = road[i-1][j]
            else:
                road[i][j] = (road[i-1][j] + road[i][j-1]) % 1000000007
                
    return road[n][m] % 1000000007