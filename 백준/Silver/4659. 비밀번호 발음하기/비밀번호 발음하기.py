import re

while True:
    password = input()
    if password == 'end':
        break

    answer, stack2, before = '', [], ''

    if re.search('[aieou]',password)==None:
        answer = 'not '
    else:
        for pw in password:
            res_2 = pw in {'a','e','i','o','u'}
            if stack2 and stack2[0]!=res_2:
                stack2 = [res_2]
            else:
                stack2.append(res_2)
            if len(stack2) == 3:
                answer = 'not '
                break

            if pw == before and pw not in {'e', 'o'}:
                answer = 'not '
                break
            else:
                before = pw

    print(f'<{password}> is {answer}acceptable.')