def solution(s):
    return ''.join([c.capitalize()+' ' for c in s.split(' ')])[:-1]
