# Calculator

def sum(m, n):
    if n >= 0:
        for el in range(n):
            m += 1
    else:
        for el in range(abs(n)):
            m -= 1
    return m


def divide(m, n):
    if m == 0 or n == 0:
        raise ZeroDivisionError
    res = 0
    isNegative = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)
    while m >= n:
        m -= n
        res += 1

    res = -res if isNegative else res
    return res


if __name__ == '__main__':
    z_set = [-2, -1, 0, 1, 2]
    sum_result = []
    for elem in z_set:
        sum_result.append(sum(elem, 1))

    div_result = []
    for elem in z_set:
        div_result.append(divide(elem, 5))