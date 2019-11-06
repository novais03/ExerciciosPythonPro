def celsius_para_farenheit():
    """ Item 10. Faça um Programa que peça a temperatura em graus Celsius,
    transforme e mostre em graus Farenheit.
                °F = °C × 1, 8 + 32
    exemplo:
    0 °C = 32 °F
    5 °C = 41 °F
    10 °C = 50 °F
    15 °C = 59 °F
    30 °C = 86 °F
    35 °C = 95 °F
    40 °C = 104 °F
    """
    c = int(input("Digite a temperatura em °C: "))
    f = float(c * 1.8 +32)

    print("A temperatura em °F é %4.2f " % f)

if __name__ == '__main__':
    celsius_para_farenheit()