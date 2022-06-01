t = int(input())     #테스트케이스 개수
for _ in range(t):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-3])  #3번째로 큰 수
