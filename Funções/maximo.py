def maximo(a,b):
    if a >= b:
        maximo = a
    else:
        maximo = b

    return maximo

if __name__ == '__main__':
    a=5
    b=6
    c = maximo(a,b)
    print(c)
