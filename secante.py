# Matheus Cabral Manoel - 9066470
# Doce


def f(x):
    return 42*x**4 + 17*x**3 + 164*x**2 + 68*x - 16


def secante(a_0, b_0, precision, max_iter):
    x = [a_0, b_0]
    f_vec = [f(x[0]), f(x[1])]
    result = {
        'value': float(0),
        'error': False,
        'error_msg': '',
        'x': x,
        'f': f_vec,
    }

    for k in range(2, max_iter):
        x.append(0.0)

        x[k] = (f(x[k-1])*x[k-2] - f(x[k-2])*x[k-1]) / (f(x[k-1]) - f(x[k-2]))
        f_vec.append(f(x[k]))

        if abs(x[k] - x[k-1]) < precision * max(1, abs(x[k])):
            result['value'] = x[k]
            return result

    result['error'] = True
    result['error_msg'] = 'Número máximo de iterações atingido.'
    return result


def calculate_error(x, result_value):
    return [abs(x_k - result_value) for x_k in x]


def print_table(result, error):
    print('{: <15}'.format('k') + '{: <12}'.format('x_k') + '{: <12}'.format('f_x_k') + '{: <12}'.format('e_k'))
    for k in range(0, len(result['x'])):
        print('{:12f}'.format(k) + '{:12f}'.format(result['x'][k]) + '{:12f}'.format(result['f'][k]) + '{:12f}'.format(error[k]))


if __name__ == '__main__':
    a_0 = float(input())
    b_0 = float(input())
    precision = float(input())
    max_iter = int(input())

    result = secante(a_0, b_0, precision, max_iter)

    if not result['error']:
        print_table(result, calculate_error(result['x'], result['value']))
