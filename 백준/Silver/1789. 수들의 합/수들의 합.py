s = int(input())
for i in range(1, s+1):    #1일 때를 생각해보면 s+1로 지정해주는게 맞다
    if s < (i*(i+1)/2):
        #'1~i까지의 합과 s'의 차이를 제외한 1~i까지의 합 요소들이 최대
        print(i-1)
        break
    elif s == (i*(i+1)/2):
        print(i)
        break