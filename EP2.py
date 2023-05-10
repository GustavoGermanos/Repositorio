def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 0:
            posicoes.append([linha,coluna])
        elif orientacao == "horizontal":
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

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for navios in frota.values():
        for navio in navios:
            for posicao2 in posicoes:
                if posicao2 in navio:
                    return False
    for posicao2 in posicoes:
        primeiro = posicao2[0] < 0
        segundo = posicao2[0] >= 10
        terceiro = posicao2[1] < 0
        quarto = posicao2[1] >= 10
        if  primeiro or segundo or  terceiro or quarto:
            return False
    return True 

#Posicionando Frota

tamanhos = {"porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino": 1}

frota = {"porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": []}

for nome_barco in frota.keys():
    
    contador = 0 

    if nome_barco == 'porta-aviões':
        i = 1
    elif nome_barco == 'navio-tanque':
        i = 2
    elif nome_barco == 'contratorpedeiro':
        i = 3
    elif nome_barco == 'submarino':
        i = 4
    
    while contador < i:
        
        print(f'Insira as informações referentes ao navio {nome_barco} que possui tamanho {tamanhos[nome_barco]}')
        
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if nome_barco != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        
        if nome_barco == 'submarino':
            orientacao = 'vertical'

        if orientacao == '1':
            orientacao = 'vertical'
        
        elif orientacao == '2':
            orientacao = 'horizontal'

        pos = posicao_valida (frota,linha,coluna,orientacao,tamanhos[nome_barco])
        if pos == False:
            print('Esta posição não está válida!')

        else:
            preenche_frota(frota,nome_barco,linha,coluna,orientacao,tamanhos[nome_barco])
            contador += 1

print(frota)
