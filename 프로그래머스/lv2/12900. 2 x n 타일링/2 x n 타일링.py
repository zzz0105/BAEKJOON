def solution(n):
    arr = [0, 1, 2] + [0]*(n-2)
    for i in range(3,n+1):
        arr[i] = ( arr[i-1] + arr[i-2] ) % 1000000007
    return arr[n] % 1000000007