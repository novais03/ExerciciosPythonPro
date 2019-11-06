def farenheit_para_celsius():
    """ Item 9. Faça um Programa que peça a temperatura em graus Farenheit,
    transforme e mostre a temperatura em graus Celsius.
                C = (5 * (F-32) / 9).
    exemplo:
    F = 212
    C = 100
    """
    f = int(input("Digite a temperatura em °F: "))
    c = float(5 * (f-32)/9)

    print("A temperatura em °C é %4.2f " % c)

if __name__ == '__main__':
    farenheit_para_celsius()