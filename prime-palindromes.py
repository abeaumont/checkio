def checkio(n):
    s = str(n)
    return not any([n % i == 0 for i in range(2, n >> 1)]) and s == s[::-1] \
        and n or checkio(n + 1)

if __name__ == '__main__':
    assert checkio(31) == 101, 'First example'
    assert checkio(130) == 131, 'Second example'
    assert checkio(131) == 131, 'Third example'
