t = int(input())    #테스트케이스 개수
for tc in range(1,t+1):
    n = int(input())
    index_1 = []    #1의 위치를 저장할 리스트
    i = 0           #현재 위치
    while(n):       #n이 0이 될 때까지
        if n%2:     ##n을 2로 나누었을 때 나머지가 1이면
            index_1.append(i)   #위치를 리스트에 추가
        i += 1      #위치 하나 증가
        n //= 2     #n을 2로 나눈 몫을 n에 대입

    print(*index_1) #인덱스의 위치들을 출력