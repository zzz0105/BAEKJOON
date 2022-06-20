def select(num):
    global energy
    if len(weights)==2:
        energy = max(energy, num)
        return
    
    for i in range(1, len(weights)-1):
        m = weights[i-1]*weights[i+1]
        p = weights.pop(i)
        select(num+m)
        weights.insert(i,p)

n = int(input())
weights = list(map(int, input().split()))
energy = 0
select(0)
print(energy)