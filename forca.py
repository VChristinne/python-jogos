import random

def jogar():

    abertura_jogo()

    palavra_secreta = seleciona_palavra_secreta()

    letras_acertadas = mostra_palavras_acertadas(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == '0'):
                print(f"Parabéns! Você encontrou todas as letras formando a palavra {palavra_secreta.upper()}")
        else:
            erros += 1  # adiciona um erro ao jogador
            print(letras_acertadas)  # índice da palavra secreta
            print(f"Ainda falta acertar {letras_faltando} letras")
            print(f"Você ainda tem {8-erros} tentativas\n")

        enforcou = erros == 8  # limite de 6 erros para enforcar
        acertou = '_' not in letras_acertadas  # quando acerta é retirado '_' das letras acertadas

        print(letras_acertadas)

    if (acertou):
        frase_vencedor()
    else:
        frase_perdedor(palavra_secreta)

    print("Fim do jogo!")

def abertura_jogo():
    print("\n*****************")
    print("* Jogo da forca *")
    print("*****************")

def seleciona_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo: 
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def mostra_palavras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
     chute = input("\nQual letra deseja chutar? ")
     chute = chute.strip().upper()
     return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
     index = 0
     for letra in palavra_secreta:
         if (chute == letra):
             letras_acertadas[index] = letra
         index += 1

def frase_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    print(f"A palavra secreta era {palavra_secreta}")

def frase_vencedor():
    print("Parabéns, você ganhou!")