N = int(input())

def han(n):
    if n < 100: return 1
    n_arr = tuple(map(int,str(n)))                  # 자릿수 튜플
    for i in range(1,len(n_arr)-1):
        if 2*n_arr[i] != n_arr[i-1] + n_arr[i+1]:   # 등차수열 확인
            return 0
    return 1
 
print(sum(han(n) for n in range(1,N+1)))