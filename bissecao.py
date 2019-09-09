# Matheus Cabral Manoel - 9066470
# Doce


from math import abs


def f(x):
    return 42*x**4 + 17*x**3 + 164*x**2 + 68*x - 16


def bissecao(a, b, precision, max_iter):
    x = []
    result = {
        'value': float(0),
        'error': false,
    }


    if f(a[0]) == 0:
        result['value'] = a[0]
        return result
    elif f(b[0]):
        result['value'] = b[0]
        return result

    if f(a[0]) * f(b[0]) > 0:
        result['error'] = true
        return result

    x[0] = a[0]
    for k in range(1, max_iter):
        x[k] = (a[k-1] + b[k-1]) / 2

        if f(x[k]) == 0 or abs(x[k] - x[k-1]) < precision * max(1, abs(x[k])):
            result['value'] = x[k]
            return result

        if f(a[k-1]) * f(x[k]) < 0:
            a[k] = a[k-1]
            b[k] = x[k]
        if f(b[k-1]) * f(x[k]) < 0:
            a[k] = x[k]
            b[k] = b[k-1]

    result['error'] = true
    return result


if __name__ == '__main__':
    a = []
    b = []
    a[0] = float(input('a0'))
    b[0] = float(input('b0'))
    precision = float(input('precision'))
    max_iter = int(input('max_iter'))

    result = bissecao(a, b, precision, max_iter)
    print(result)
