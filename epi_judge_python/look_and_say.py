from test_framework import generic_test


def next_num(s: str) -> str:
    (count, digit, res) = (1, s[0], [])
    for i in range(1, len(s)):
        if s[i] == digit:
            count += 1
        else:
            res += [str(count), digit]
            count = 1
            digit = s[i]
    return ''.join(res + [str(count), digit])


def look_and_say(n: int) -> str:
    val = '1'
    for i in range(1, n):
        val = next_num(val)
    return val


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
