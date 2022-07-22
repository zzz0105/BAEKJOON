def solution(absolutes, signs):
    answer = 0
    nums = list(zip(absolutes, signs))
    for num in nums:
        if num[1] == True:
            answer += num[0]
        else:
            answer -= num[0]
    return answer