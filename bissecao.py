# Matheus Cabral Manoel - 9066470
# Doce


def f(x):
    return 42*x**4 + 17*x**3 + 164*x**2 + 68*x - 16


def bissecao(a_0, b_0, precision, max_iter):
    x = [0.0]
    a = [a_0]
    b = [b_0]
    f_vec = []
    result = {
        'value': float(0),
        'error': False,
        'x': x,
        'a': a,
        'b': b,
        'f': f_vec,
    }


    if f(a[0]) == 0:
        result['value'] = a[0]
        return result
    elif f(b[0]) == 0:
        result['value'] = b[0]
        return result

    if f(a[0]) * f(b[0]) > 0:
        result['error'] = True
        return result

    x[0] = a[0]
    f_vec.append(f(x[0]))
    for k in range(1, max_iter):
        x.append(0.0)
        a.append(0.0)
        b.append(0.0)

        x[k] = (a[k-1] + b[k-1]) / 2
        f_vec.append(f(x[k]))

        if f(x[k]) == 0 or abs(x[k] - x[k-1]) < precision * max(1, abs(x[k])):
            result['value'] = x[k]
            return result

        if f(a[k-1]) * f(x[k]) < 0:
            a[k] = a[k-1]
            b[k] = x[k]
        elif f(b[k-1]) * f(x[k]) < 0:
            a[k] = x[k]
            b[k] = b[k-1]

    result['error'] = True
    return result


def calculate_error(x, result_value):
    return [abs(x_k - result_value) for x_k in x]


def print_table(result, error):
    print('{: <15}'.format('k') + '{: <12}'.format('a') + '{: <12}'.format('b') + '{: <12}'.format('x_k') + '{: <12}'.format('f_x_k') + '{: <12}'.format('e_k'))
    for k in range(1, len(result['x'])):
        print('{:12f}'.format(k) + '{:12f}'.format(result['a'][k]) + '{:12f}'.format(result['b'][k]) + '{:12f}'.format(result['x'][k]) + '{:12f}'.format(result['f'][k]) + '{:12f}'.format(error[k]))



if __name__ == '__main__':
    a_0 = float(input('a0: '))
    b_0 = float(input('b0: '))
    precision = float(input('precision: '))
    max_iter = int(input('max_iter: '))

    result = bissecao(a_0, b_0, precision, max_iter)

    if not result['error']:
        print(result)
        print(f(result['value']))
        print('a: ' + str(result['a']))
        print('b: ' + str(result['b']))
        print('x: ' + str(result['x']))
        print('error: ' + str(calculate_error(result['x'], result['value'])))
        print_table(result, calculate_error(result['x'], result['value']))
