def jogada(n):
    """funcao que pega as jogadas dos jogadores"""
    while n==1:
        j=int(input("\n Jogador 1, faca sua jogada, escolha a posição da sua peca X: "))
        if 0<j<10:
            return j
        else:
            print("\n JOGADA INVÁLIDA! TENTE NOVAMENTE \n")
        
    while n==2:
        j=int(input("\n Jogador 2, faça sua jogada, escolha a posição da sua peça O: "))
        if 0<j<10 : 
            return j
        else:
            print("\n JOGADA INVÁLIDA! TENTE NOVAMENTE \n")