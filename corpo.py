from jog import jogada
from tabuleiro import tabuleiro
from turno import turno
from fim import fim
def corpo():
    pecas = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}  #dicionario de posicoes das pecas
    t=1
    tabuleiro(pecas)
    while True:
        while turno(t)==1:
            j = jogada(1)
            if pecas[j] == "X" or pecas[j] == "O":
                print("\n  !! JOGADA INVÁLIDA !! TENTE NOVAMENTE! \n") 
            else:
                pecas[j] = 'X' #substitui o número fornecido pelo jogador pela sua peca no tabuleiro
                t+=1         
        tabuleiro(pecas)
        fim(pecas)
        while turno(t)==2:
            j = jogada(2)
            if pecas[j] == "X" or pecas[j] == "O":
                print("\n  !! JOGADA INVÁLIDA !! TENTE NOVAMENTE! \n")                
            else:
                pecas[j] = 'O' #substitui o número fornecido pelo jogador pela sua peca no tabuleiro
                t+=1                
        tabuleiro(pecas)
        fim(pecas)
        if t==8:
            print("\n   EMPATE \n")
            break
        