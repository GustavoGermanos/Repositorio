def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "horizontal":
            posicao = [linha, coluna+i]
            posicoes.append(posicao)
        elif orientacao == "vertical":
            posicao = [linha+i, coluna]
            posicoes.append(posicao)
    return posicoes

def preenche_frota (frota, nome, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome not in frota:
        frota[nome] = []
    frota[nome].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


