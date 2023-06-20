def solution(s):
    py = {'p':0, 'y':0}

    for c in s.lower():
        if c=='p' or c=='y':
            py[c] += 1

    return py['p'] == py['y']