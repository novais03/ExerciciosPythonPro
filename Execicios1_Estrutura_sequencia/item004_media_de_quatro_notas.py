def media_de_quatro_notas():
    """Item 4.Faça um Programa que peça as 4 notas bimestrais e mostre a média."""
    n1 = float(input("Digite a nota do 1° bimestre: "))
    n2 = float(input("Digite a nota do 2° bimestre: "))
    n3 = float(input("Digite a nota do 3° bimestre: "))
    n4 = float(input("Digite a nota do 4° bimestre: "))
    media=((n1+n2+n3+n4)/4)
    print('A media dos quatro bimestres é de %4.2f' % media)

if __name__ == '__main__':
    media_de_quatro_notas()

