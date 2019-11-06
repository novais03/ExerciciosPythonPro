def calculo_salario():
    """Item 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.
    """
    valor_hora = float(input("Qual o valor da hora trabalhada: "))
    horas_trabalhadas_mes = int(input("qts horas você trabalhou no mês: "))

    print("R$ %10.2f " % (valor_hora * horas_trabalhadas_mes))

if __name__ == '__main__':
    calculo_salario()