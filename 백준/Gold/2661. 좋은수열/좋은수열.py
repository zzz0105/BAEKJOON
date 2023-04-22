def check(nums):
    for i in range(1, len(nums)//2+1):
        if nums[-i:]==nums[-2*i:-i]:
            return False
    return True

def choose(nums):
    if len(nums)==N:
        print(''.join(nums))
        exit(0)
    for num in ('1','2','3'):
        if check(nums+[num]):
            choose(nums+[num])

N = int(input())
print(choose([]))