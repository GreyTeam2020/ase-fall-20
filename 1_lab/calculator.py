# Calculator

def sum(m, n):
    for at in range(0, n):
        if m >= 0:
            return m + 1
        else:
            return m - 1


def divide(m, n):
    result = 0
    while m > 0:
        result = +1
        m -= n
    return result


if __name__ == '__main__':
    z_set = [-2, -1, 0, 1, 2]
    sum_result = []
    for elem in z_set:
        sum_result.append(sum(elem, 1))

    div_result = []
    for elem in z_set:
        div_result.append(divide(elem, 5))