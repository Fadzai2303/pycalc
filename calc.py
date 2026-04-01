def compute(expression):
    values = expression.split(' ')
    num0 = int(values[0])
    operator1 = values[1]
    num1 = int(values[2])
    if operator1 == '+':
        return num0 + num1
    elif operator1 == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None