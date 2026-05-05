import numpy as np

mapa = np.random.randint(1,10 ,size=(5,5))

while True:
    tesouro_linha, tesouro_coluna = np.random.randint (0,5, size=2)
    if (tesouro_linha,tesouro_coluna) != (0,0):
        break
    
posicao_jogador = (0,0)
pontuacao = 0
def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador =mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1
    print("\nMapa Atual:")

    for linha in mapa_com_jogador:
        print(" ".join(f"{item:2d}" for item in linha))


while True:
    mostrar_mapa(mapa, posicao_jogador)
    direcao = input("Informe a direção!!!").strip().lower()
    movimentos = {
        "c": (-1,0),
        "b": (1,0),
        "e": (0,-1),
        "d": (0,1),
    }
    if direcao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcao][0], posicao_jogador[1] + movimentos[direcao][1])
    else:
        print("Direção invalida")
    if not (0 <= nova_posicao[0] < mapa.shape[0] and 0<= nova_posicao[1] < mapa.shape[1]):
        print("Fora do mapa tente novamente")
        continue
    posicao_jogador = nova_posicao
    pontuacao +=1

    if posicao_jogador == (tesouro_linha,tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print("\n\n********Este deu trabalho********")
        print(f"Pontuação: {pontuacao}")
        print(f"O premio estava em: {(tesouro_linha, tesouro_coluna)}")