def soma():
    """Item 3. Faça um Programa que peça dois números e imprima a soma."""

    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número.: '))
    return(a+b)

if __name__ == '__main__':
    print('Soma dos 02 números é: %d' % soma())