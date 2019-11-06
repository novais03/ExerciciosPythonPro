import epar

def par_ou_impar(x):
    if epar.epar(x):
        resultado = 'par'
    else:
        resultado = 'impar'

    return resultado

if __name__ == '__main__':
    print(par_ou_impar(4))
