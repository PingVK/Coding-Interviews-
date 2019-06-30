"""
page51, problem 5
将字符串中每个空格替换成【%20】
"""


def replace_blank(s: str) -> str:
    if not s:
        return ''
    count = 0
    for e in s:
        if e == ' ':
            count += 1
    if count == 0:
        return s

    new_len = len(s) + count * 2
    new_lst = [''] * new_len
    i = new_len - 1
    for e in s[::-1]:
        if e == ' ':
            new_lst[i] = '0'
            new_lst[i-1] = '2'
            new_lst[i-2] = '%'
            i -= 3
        else:
            new_lst[i] = e
            i -= 1
    return ''.join(new_lst)


if __name__ == '__main__':
    case1 = ' Hello  World '
    case2 = '    '
    case3 = 'hello_world'
    case4 = ''
    cases = [case1, case2, case3, case4]
    for case in cases:
        print(replace_blank(case))
