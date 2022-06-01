passenger = 0   #기차 안 승객
max_passenger = 0   #승객 최대값
for stop in range(10):  #정차역 10개
    n, m = map(int, input().split())    #내린 승객, 탄 승객
    passenger += (- n + m)
    if passenger > max_passenger:   #현재 승객이 최대 승객보다 많다면
        max_passenger = passenger
print(max_passenger)