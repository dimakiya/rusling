def evaluate_expression(expr, variables):
    # вычисление выражений с поддержкой //
    expr = expr.replace('//', '//')
    for var_name, var_value in variables.items():
        expr = expr.replace(var_name, str(var_value))
    return eval(expr)

def is_string(value):
    return value.startswith('"') and value.endswith('"')
