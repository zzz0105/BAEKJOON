n = int(input())    #정수의 개수
nums = list(map(int, input().split()))   #입력한 정수들
min_num = max_num = nums[0] #최소값, 최댓값을 저장할 변수 지정
for num in nums:
    if num > max_num:   #현재 최대값보다 크다면
        max_num = num
    elif num < min_num: #현재 최소값보다 작다면
        min_num = num
print(min_num, max_num)