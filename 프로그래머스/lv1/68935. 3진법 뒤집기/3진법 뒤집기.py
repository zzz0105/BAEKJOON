def solution(n):
    ternary = ''    # n을 앞뒤 반전된 삼진법으로 변환
    answer = 0
    while n:
        ternary += str(n % 3)
        n //= 3
    for i in range(len(ternary)):
        answer += int(ternary[i]) * 3**(len(ternary)-i-1)
    return answer