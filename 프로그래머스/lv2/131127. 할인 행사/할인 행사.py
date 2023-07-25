def solution(want, number, discount):
    wd = {}         # 원하는 것: 개수
    dd = {}         # 할인하는 물건: 구매 가능한 개수
    possible = {}   # 물건: 구매가능 여부
    for i in range(len(want)):
        wd[want[i]] = number[i]
        dd[want[i]] = 0
        possible[want[i]] = False
        
    days = 0        # 가능한 날
    for i in range(len(discount)):
        if i >= 10:
            item = discount[i-10]
            dd[item] -= 1
            if item in wd.keys():
                possible[item] = dd[item] >= wd[item]
                
        item = discount[i]
        dd[item] = dd.get(item,0) + 1
        if item in wd.keys():
            possible[item] = dd[item] >= wd[item]  
        if False not in possible.values():
            days += 1
            
    return days