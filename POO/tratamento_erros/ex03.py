def divide(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print('Não é possível divisão por zero!')
    else:
        print('resultado', resultado)



divide(5,3)
