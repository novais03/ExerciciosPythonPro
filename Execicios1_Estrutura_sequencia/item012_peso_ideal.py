def peso_ideal():
    """Item 13. Tendo como dado de entrada a altura (h) de uma pessoa,
    construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        Para homens: (72.7h) - 58
        Para mulheres: (62.1h) - 44.7
    Exemplo:
    altura....: 1.8
    homens....: 72,86
    malheres..: 67,08
    """

    h = float(input("qual a sua altura:"))
    s = input("sexo masculino (m) ou feminino (f):")

    if s == 'm':
        peso = float((h * 72.7) - 58)
        print("%3.2f" % peso)
    elif s == 'f':
        peso = float((h * 62.1) - 44.7)
        print("%3.2f" % peso)
    else:
        print("sexo invalido!")

if __name__ == '__main__':
    peso_ideal()