def fim(pecas):
    if pecas[1]==pecas[2]==pecas[3]=="X" or pecas[4]==pecas[5]==pecas[6]=="X" or pecas[7]==pecas[8]==pecas[9]=="X" or pecas[1]==pecas[4]==pecas[7]=="X" or pecas[2]==pecas[5]==pecas[8]=="X" or pecas[3]==pecas[6]==pecas[9]=="X" or pecas[1]==pecas[5]==pecas[9]=="X" or pecas[3]==pecas[5]==pecas[7]=="X":
        print("----------FIM DE JOGO----------- \n                JOGADOR 1 VENCEU! \n")
        return False
    elif pecas[1]==pecas[2]==pecas[3]=="O" or pecas[4]==pecas[5]==pecas[6]=="O" or pecas[7]==pecas[8]==pecas[9]=="O" or pecas[1]==pecas[4]==pecas[7]=="O" or pecas[2]==pecas[5]==pecas[8]=="O" or pecas[3]==pecas[6]==pecas[9]=="O" or pecas[1]==pecas[5]==pecas[9]=="O" or pecas[3]==pecas[5]==pecas[7]=="O":
        print("----------FIM DE JOGO----------- \n                JOGADOR 2 VENCEU! \n")
        return False
    else:
        return True 