from turno import turno
def jogada():
    """funcao que pega as jogadas dos jogadores"""
    pecas = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
    t=1
    turno(t)
    while turno(t)==1:
        j=int(input("\n Jogador 1, faça sua jogada, escolha a posição da sua peça X: "))
        if j>0 and j<10 and pecas[j]!="X" and pecas[j]!="O":
            pecas[j] = 'X' #substitui o número fornecido pelo jogador pela sua peca no tabuleiro
            t+=1
            continue
        else:
            print("Jogada invalida, tente de novo")
            continue
    while turno(t)==2:
        j=int(input("\n Jogador 2, faça sua jogada, escolha a posição da sua peça O: "))
        if j>0 and j<10 and pecas[j]!="X" and pecas[j]!="O":
            pecas[j] = 'O' #substitui o número fornecido pelo jogador pela sua peca no tabuleiro
            t+=1
            continue
        else:
            print("Jogada invalida, tente de novo")
            continue
    
        


