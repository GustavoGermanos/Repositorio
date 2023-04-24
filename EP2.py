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