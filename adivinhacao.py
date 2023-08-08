from random import randrange

def abertura_jogo():
    print("\n***********************")
    print("* Jogo da adivinhação *")
    print("***********************")

def jogar():
    abertura_jogo()

    print("Níveis do jogo:\n")
    print("(1) - nível 1 com 20 tentativas\n")
    print("(2) - nível 2 com 10 tentativas\n")
    print("(3) - nível 3 com 5 tentativas\n")
    nivel = int(input("Selecione um nível: "))

    if (nivel == 1):
        total_tentativas = 20

    elif (nivel == 2):
        total_tentativas = 10

    elif (nivel == 3):
        total_tentativas = 5

    elif (nivel > 3):
        print("Nível não encontrado, digite um nível existente\n")
        jogar()

    numero_secreto = randrange(100)  # valor aleatório a ser adivinhado
    rodada = 1  # rodada que o usuário começa o jogo
    pontos = 1000  # jogador começa o jogo com 1000 pontos 

    for rodada in range(1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}\n")

        # resposta do usuário
        chute = int(input("Digite um número: "))

        acertou = chute == numero_secreto  # chute igual ao numero_secreto acertou
        maior = chute > numero_secreto  # chute maior que o numero_secreto
        menor = chute < numero_secreto  # chute menor que o numero_secreto

        if (acertou):
            print("\nParabéns, você adivinhou o número!")
            print(f"Você ganhou {pontos} pontos")
            break

        elif (maior):
            print("Você errou! O seu chute foi maior que o número secreto\n")

        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto\n")

        ponto_perdidos = abs(chute - numero_secreto)
        pontos -= ponto_perdidos

    print('\nFim do jogo!')