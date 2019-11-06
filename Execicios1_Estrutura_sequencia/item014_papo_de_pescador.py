def papo_de_pescador():

    """Item 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
    diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
    de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
    João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.

    Gravar na variável excesso a quantidade de quilos além do limite
    e na variável multa o valor da multa que João deverá pagar.
    Imprima os dados do programa com as mensagens adequadas.

    Exemplo:
    Peso = 60
    execesso = 10
    multa_a_pagar = R$ 40.00
    """
    x = float(input("total de peso: "))
    max = float(50.00)
    multa = float(4.00)

    if x > 50.00:
        excesso = (x - 50.00)
        multa_a_pagar = excesso * multa
        print("O valor da multa a pagar é de: %4.2f" % multa_a_pagar)
    else:
        print("O peso não excedeu a o limite de 50 kg")

if __name__ == '__main__':
    papo_de_pescador()