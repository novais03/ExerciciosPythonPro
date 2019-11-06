def area_qaudrado_e_dodro():
    """Item 7. Faça um Programa que calcule a área de um quadrado,
    em seguida mostre o dobro desta área para o usuário.
    """
    lado = int(input("digite o valor do lado do qaudrado: "))
    area = lado**2
    dobro_da_area = area*2

    print("area %d" %area)
    print("Dobro da area %d" % dobro_da_area)

if __name__ == '__main__':
    area_qaudrado_e_dodro()