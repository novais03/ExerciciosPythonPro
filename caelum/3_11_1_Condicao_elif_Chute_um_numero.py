"""
    atribuir um valor para uma variável numero e pedir para o usuário entrar com um valor.
    caso o chute não seja igual ao número secreto, podemos dar uma pista para o usuário se
    ele foi maior ou menor do que o chute inicial.
    Ou seja, devemos acrescentar esse tratamento caso o usuário erre o chute:

    Se chute = número:
        "Você acertou!"
    Senão:
        Se chute maior do que número_secreto:
            "Você errou! O seu chute foi maior que o número secreto"
        Senão
            "Você errou! O seu chute foi menor que o número secreto"

"""
print('*********************')
print('* JOGO DA ADIVINAÇÃO*')
print('*********************')

numero_secreto = 42
chute = int(input('Digite o Número: '))

acertou = numero_secreto == chute

if (acertou):
    print('Você acertou')
elif chute > 42:
    print('Você errou! O seu chute foi maior que o número secreto')
else:
    print('Você errou! O seu chute foi menor que o número secreto')


