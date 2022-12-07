import random

global matriz,numPossiveis,stop,matrizPronta,posicoes;
matriz = []
stop = 0
numPossiveis = [1,2,3,4,5,6,7,8,9]
matrizPronta = []
posicoes = []

# i representa linha e j coluna
def iniciaVazia():
    global matriz
    for i in range(0,9):
        linha = []
        for j in range(0,9):
            linha.append(0)
        matriz.append(linha)

def mapearPosicoes(matriz):
    global posicoes
    contador = 0 
    for i in range(0,9):
        for j in range(0,9):
            if(matriz[i][j]==0):
                posicoes.append(contador)
            contador = contador + 1
            
def confereRegra(escolhido,i,j,matriz):
    
    erro = 0
    subNumber = 0
    linha = matriz[i]
    if(escolhido in linha):
        erro = 1
    coluna = []
    for l in matriz:
        coluna.append(l[j])
    if(escolhido in coluna):
        erro = 1

    #conferindo a sub-matriz

    #primeira linha
    if(i>=0 and i<3):
        if(j>=0 and j<3):
            subNumber = 1
    if(i>=0 and i<3):
        if(j>2 and j<6):
            subNumber = 2
    if(i>=0 and i<3):
        if(j>5 and j<=8):
            subNumber = 3

    #segunda linha
    if(i>2 and i<6):
        if(j>=0 and j<3):
            subNumber = 4
    if(i>2 and i<6):
        if(j>2 and j<6):
            subNumber = 5
    if(i>2 and i<6):
        if(j>5 and j<=8):
            subNumber = 6

    #terceira linha
    if(i>5 and i<=8):
        if(j>=0 and j<3):
            subNumber = 7
    if(i>5 and i<=8):
        if(j>2 and j<6):
            subNumber = 8
    if(i>5 and i<=8):
        if(j>5 and j<=8):
            subNumber = 9

    #final das verificações
    subMatriz=[]
    #pegando a sub-matriz para verificação de erros
    #primeira linha
    if(subNumber==1):
        for i in range(0,3):
            for j in range(0,3):
                subMatriz.append(matriz[i][j])
    elif(subNumber==2):
        for i in range(0,3):
            for j in range(3,6):
                subMatriz.append(matriz[i][j])
    elif(subNumber==3):
        for i in range(0,3):
            for j in range(6,9):
                subMatriz.append(matriz[i][j])
    #segunda linha
    elif(subNumber==4):
        for i in range(3,6):
            for j in range(0,3):
                subMatriz.append(matriz[i][j])
    elif(subNumber==5):
        for i in range(3,6):
            for j in range(3,6):
                subMatriz.append(matriz[i][j])
    elif(subNumber==6):
        for i in range(3,6):
            for j in range(6,9):
                subMatriz.append(matriz[i][j])
    #terceira linha
    elif(subNumber==7):
        for i in range(6,9):
            for j in range(0,3):
                subMatriz.append(matriz[i][j])
    elif(subNumber==8):
        for i in range(6,9):
            for j in range(3,6):
                subMatriz.append(matriz[i][j])
    elif(subNumber==9):
        for i in range(6,9):
            for j in range(6,9):
                subMatriz.append(matriz[i][j])
    #final da subMatriz
    if(escolhido in subMatriz):
        erro = 1
    if(erro > 0):

        return True
    else:

        return False

def montaJogo(pos,matriz):
    global stop,matrizPronta,posicoes
    printaMatriz(matriz)
    if(pos == 81 and stop==0):
        
        stop=1
        for i in range(0,9):
            matrizPronta.append([])
            for j in range(0,9):
                matrizPronta[i].append(matriz[i][j])
    elif(stop==0 and (pos in posicoes)):
        random.shuffle(numPossiveis)
        linha = pos // 9
        coluna = pos % 9
        for e in numPossiveis:
            if(not confereRegra(e,linha,coluna,matriz)):
                matriz[linha][coluna] = e
                montaJogo(pos+1,matriz)
                matriz[linha][coluna]=0
           
    elif(pos not in posicoes):
        montaJogo(pos+1,matriz)

def montaJogo2(pos,matriz):
    if(pos == 81):
        print(matriz)
        for i in range(0,9):
            matrizPronta.append([])
            for j in range(0,9):
                matrizPronta[i].append(matriz[i][j])
    else:
        linha = pos // 9
        coluna = pos % 9
        if(matriz[linha][coluna]==0):
            for value in numPossiveis:
                if(not confereRegra(value,linha,coluna,matriz)):
                    matriz[linha][coluna]=value
                    montaJogo2(pos+1,matriz)
            matriz[linha][coluna]=0
        else:
            montaJogo2(pos+1,matriz)
            
def printaMatriz(matrizPronta):
    print("--------------------------")
    for i in range(0,9):
        if(i%3==0 and i != 0):
            print("--------------------------")
        for j in range(0,9):
            if(j%3==0):
                print("| ",end="")
            print("{} ".format(matrizPronta[i][j]),end="")
        print("|")
    print("--------------------------")
    
iniciaVazia()
#testando o solver
matrizTeste=[]
matrizTeste.append([0,4,0,8,3,0,5,0,0])
matrizTeste.append([0,0,0,0,4,5,0,3,0])
matrizTeste.append([5,0,0,1,0,6,0,0,4])
matrizTeste.append([0,0,0,0,0,4,0,6,0])
matrizTeste.append([2,8,7,0,0,3,0,5,9])
matrizTeste.append([0,6,9,0,0,0,3,8,1])
matrizTeste.append([0,9,2,0,7,0,1,0,5])
matrizTeste.append([8,0,5,0,2,0,0,7,3])
matrizTeste.append([7,3,0,0,0,0,0,9,8])
#fim do teste

mapearPosicoes(matrizTeste)
montaJogo2(0,matrizTeste)
printaMatriz(matrizPronta)
