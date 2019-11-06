import math
def area_circulo():
    """Item 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área"""
    raio = int(input("digite o valor do raio: "))
    area = float((math.pi)*(raio**raio))

    print("%5.4f" % area)

if __name__ == '__main__':
    area_circulo()