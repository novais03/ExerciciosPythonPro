def calculos_diversos():
    """Item 11. Faça um Programa que peça 2 números inteiros e um número real.
    Calcule e mostre:
    int1 = 10
    int2 = 20
    real = 2.5
     * o produto do dobro do primeiro com metade do segundo .
        resp1 = (10*2) / (20/2)
        resp1 = 20 / 10
        resp1 = 2.00
     * a soma do triplo do primeiro com o terceiro.
        resp2 = (10 * 3) + 2.5
        resp2 = 32.5
     * o terceiro elevado ao cubo.
        resp3 = 2.5**3
        resp3 = 15.625
     """
    int1 = int(input("Digite o 1° número (inteiro): "))
    int2 = int(input("Digite o 2° número (inteiro): "))
    real = float(input("Digite p 3° Número (real... :)"))

    #calculos
    resp1 = (int1*2) / (int2/2)
    resp2 = (int1*3) + real
    resp3 = (real**3)

    print(resp1, resp2, resp3)

if __name__ == '__main__':
    calculos_diversos()