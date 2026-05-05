import numpy as np
def colocar_peca(tabuleiro, linha, coluna, peca):
    tabuleiro[linha][coluna] = peca

def verifica_vitoria(tabuleiro,peca):
    linhas = np.any(np.all(tabuleiro==peca, axis=1))
    colunas = np.any(np.all(tabuleiro==peca,axis=0))
    diagonais= np.all(np.diag(tabuleiro)==peca)or np.all(np.diag(np.fliplr(tabuleiro))==peca)
    return linhas or colunas or diagonais

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(str(x)if x != 0 else"" for x in linha))
        print("-"*8)

def jogo():
    tabuleiro =np.zeros((3,3), dtype=int)
    peca_atual = 1
    vencedor = False
    empate = False

    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro)
        while True:
            try:
                linha = int(input(f"jogador {peca_atual}, escolha a linha(0,1,2):"))
                coluna = int(input(f"jagador {peca_atual}, escolha a coluna (0,1,2):"))
                if linha not in [0,1,2] or coluna not in [0,1,2]:
                    print("\nEsccolha numeros validos 0 1 2\n")
                    continue
                if tabuleiro [linha][coluna] !=0:
                    print("Ja esta marcado")
                    continue
                colocar_peca(tabuleiro,linha,coluna, peca_atual)
                vencedor = verifica_vitoria(tabuleiro,peca_atual)
                if np.all(tabuleiro !=0):
                    empate=True
                break


            except ValueError:
                print("\nEntrada invalida!!Usar numero de 0 a 2.\n")
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    imprimir_tabuleiro(tabuleiro)
    if vencedor:
        print(f"\n\n\tVoce venceu {peca_atual}")
    else:
        print("Empate")
jogo()