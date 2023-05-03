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

def posiciona_frota (frota):

    tabuleiro = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

    for navio, posicoes in frota.items():
        for posicao in posicoes:
            for eixo in posicao:
                tabuleiro[eixo[0]][eixo[1]] = 1

    return tabuleiro

def afundados (frota, tabuleiro):
    afundado_x = 0
    for tipo in frota:
        for posicoes in frota[tipo]:
            afundado_y = 0
            for posicao in posicoes:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    afundado_y += 1
            if afundado_y == len(posicoes):
                afundado_x += 1
    return afundado_x