"""
    atribuir um valor para uma variável numero e pedir para o usuário entrar com um valor.
    Devemos verificar se os valores são iguais como um jogo de adivinhação em que o usuário deve adivinhar
     o número definido.

     Se chute igual a número (42) : "Você acertou"
    Se chute diferente de número: "Você errou"
"""
numero = 42
chute = int(input('Digite o Número: '))

if chute == 42:
    print('Você acertou')
else:
    print('Você errou!')

