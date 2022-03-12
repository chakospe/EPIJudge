from test_framework import generic_test


def snake_string(s: str) -> str:
    top, middle, bottom = [], [], []
    which = 'mt'
    for i in s:
        if which[0] == 'm':
            middle.append(i)
            which = which[1]
        elif which == 't':
            top.append(i)
            which = 'mb'
        else:
            bottom.append(i)
            which = 'mt'
    return ''.join([''.join(top), ''.join(middle), ''.join(bottom)])


# avg/med: 4 us/3 us
# def snake_string(s: str) -> str:
#     top, middle, bottom = [], [], []
#     which = 'mt'
#     for i in s:
#         if which[0] == 'm':
#             middle.append(i)
#             which = which[1]
#         elif which == 't':
#             top.append(i)
#             which = 'mb'
#         else:
#             bottom.append(i)
#             which = 'mt'
#     return ''.join([''.join(top), ''.join(middle), ''.join(bottom)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
