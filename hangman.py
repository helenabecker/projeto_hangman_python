import random
import os

# JOGO DA FORCA

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

desenhos = [
    """
     ______
     |     |
     |
     |
     |
    _|_
    """,
    """
     ______
     |     |
     |     O
     |
     |
    _|_
    """,
    """
     ______
     |     |
     |     O
     |     |
     |
    _|_
    """,
    """
     ______
     |     |
     |     O
     |    /|
     |
    _|_
    """,
    """
     ______
     |     |
     |     O
     |    /|\\
     |
    _|_
    """,
    """
     ______
     |     |
     |     O
     |    /|\\
     |    /
    _|_
    """,
    """
     ______
     |     |
     |     O
     |    /|\\
     |    / \\
    _|_
    """
]

def desenho(erros):
    print(desenhos[erros])

# definir função que pergunta palpite do jogador
def pedir_palpite():
    while True:
        palpite = input("\nSeu palpite: ").lower()
        if len(palpite) == 1 and palpite.isalpha():
            return palpite
        print("Digite apenas uma letra.")

# definir função para conferir palpite do jogador
def conferir_palpite(palpite, palavra_escolhida, palavra_mostrada):
    acertos = 0 # conta o numero de acertos
    nova_palavra = list(palavra_mostrada)  # transforma em lista para editar

    for i, letra in enumerate(palavra_escolhida):
        if letra == palpite:  # confere cada letra da palavra final para ver se é igual o palpite
            nova_palavra[i] = palpite # revela as letras corretas ao jogador
            acertos += 1

    palavra_atualizada = "".join(nova_palavra)
    return acertos > 0, palavra_atualizada


# cria uma lista de palavras e sorteia uma para o jogo
lista_palavras = ["fruta", "computador", "agua", "bacalhau", "calor", "comestivel", "poeira", "sabedoria"]
palavra_escolhida = random.choice(lista_palavras)

# cria palavra secreta para mostrar ao jogador
palavra_mostrada = "_" * len(palavra_escolhida)

erros = 0
# derrota acontece quando houverem 6 erros
# jogador ganha quando a palavra
while erros < 6:
    clear_terminal()
    print("JOGO DA FORCA\n")
    print(palavra_mostrada)
    desenho(erros)
    
    palpite = pedir_palpite()

    acerto, palavra_mostrada = conferir_palpite(palpite, palavra_escolhida, palavra_mostrada)
    if not acerto:
        erros += 1
    elif palavra_mostrada == palavra_escolhida:
        print("\nParabens, acertou todas as letras!")
        print(f"A palavra era: {palavra_escolhida}\n")
        break
else: 
    clear_terminal()
    print("JOGO DA FORCA")
    desenho(erros)
    print("\nPoxa, foi derrotado...")
    print(f"A palavra era: {palavra_escolhida}\n")