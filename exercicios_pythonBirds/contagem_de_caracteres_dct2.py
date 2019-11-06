def contar_caracteres(s):

    """ função que conta os caracteres de uma string

    Ex:
    >>> contar_caracteres('renzo')
    {'e' : 1, 'n' : 1, 'o' : 1, 'r' : 1, 'z' : 1}

    >>> contar_caracteres('banana')
    {'a' : 3, 'b' : 1, 'n' : 2

    :param s: Strin a ser contada
    """
    resultado = {}

    for caracter in s:
       # contagem = resultado.get(caracter, 0)
       # contagem += 1
       # resultado[caracter] = contagem
        resultado[caracter] =resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))

