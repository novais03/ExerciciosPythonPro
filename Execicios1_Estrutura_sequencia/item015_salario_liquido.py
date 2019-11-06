def salario_liquido():
    """
    Item 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
     8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    1) salário bruto.
    2)quanto pagou ao INSS.
    3) quanto pagou ao sindicato.
    4)o salário líquido.
    *calcule os descontos e o salário líquido, conforme a tabela abaixo:
        +Salário Bruto : R$ 14300.00
        -IR (11%) : R$  1573.00
        -INSS (8%) : R$ 1144.00
        -Sindicato ( 5%) : R% 715.00
        =Salário Liquido : R$ 10868.00

    Obs.: Salário Bruto - Descontos = Salário Líquido.
    Exmplo
    Valor Hora: 65,00
    qt horas: 220

   """
    valor_hora = float(input('Qual o preço da hora trab...: '))
    horas_trabalhadas = int(input('Qual a quantidade de horas trabalhadas: '))

    salario_bruto = valor_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05

    print(" +Salário Bruto....: R$ %5.2f" %salario_bruto)
    print(" -IR (0.11)........: R$ %5.2f" %ir)
    print(" -INSS (0.08)......: R$ %5.2f" %inss)
    print(" -SINDICATO (0.05).: R$ %5.2f" %sindicato)
    print(" =Salário Líquido..: R$ %5.2f" %(salario_bruto-ir-inss-sindicato))

if __name__ == '__main__':
    salario_liquido()