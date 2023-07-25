def solution(want, number, discount):
    wd = {} # 원하는 것: 개수
    dd = {} # 할인하는 물건: 구매 가능한 개수
    for i in range(len(want)):
        wd[want[i]] = number[i]
        dd[want[i]] = 0
        
    days = 0 # 가능한 날
    for i in range(len(discount)):
        if i >= 10:
            dd[discount[i-10]] -= 1
        dd[discount[i]] = dd.get(discount[i],0) + 1
        
        flag = 0
        for item, ea in wd.items():
            if dd[item] < ea:
                break
        else:
            days += 1    

    return days