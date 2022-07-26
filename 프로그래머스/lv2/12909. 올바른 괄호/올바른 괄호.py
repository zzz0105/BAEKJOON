def solution(s):
    stack = []
    for t in s:
        if t=='(':
            stack.append('(')
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True if not stack else False