import adivinhacao
import forca

print('\n*********************')
print('*** Menu de jogos ***')
print('*********************')

print('\n1. Adivinhação')
print('2. Forca')

escolha = int(input('\nDigite o número do jogo: '))

if escolha == 1:
    adivinhacao.jogar()

elif escolha == 2:
    forca.jogar()
