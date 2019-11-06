def metros_em_centimetros():
    """item 5. Faça um Programa que converta metros para centímetros."""
    m = float(input("digite a quantidade de metros: "))
    c = int(m*100)

    print("%4.2f metros correspondem a %d centimetros" % (m,c))

if __name__ == '__main__':
    metros_em_centimetros()
