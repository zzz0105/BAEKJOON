from math import ceil

nums = input()
n_dict = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
for n in nums:
    if n == '9':
        n = '6'
    n_dict[n] += 1
n_dict['6'] = ceil((n_dict['6'])/2)
print(max(n_dict.values()))