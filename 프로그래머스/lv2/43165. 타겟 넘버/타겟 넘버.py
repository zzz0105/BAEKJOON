def solution(numbers, target):
    cnt = 0
    def cal(depths, value):
        if depths==len(numbers):
            if value==target:
                nonlocal cnt
                cnt += 1
            return
        cal(depths+1, value+numbers[depths])
        cal(depths+1, value-numbers[depths])
    cal(0, 0)
    return cnt