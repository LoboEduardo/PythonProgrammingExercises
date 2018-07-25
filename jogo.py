from turno import turno
def jogo():
	pecas = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
	t=1
	turno(t)
	while True:
		while turno(t)==1:
			j=int(input("\n Jogador 1, faça sua jogada, escolha a posição da sua peça X: "))
			if j>0 and j<10 and pecas[j]!="X" and pecas[j]!="O":
				pecas[j] = 'X' #substitui o número fornecido pelo jogador pela sua peca no tabuleiro
				t+=1
				continue
			else:
				print("Jogada invalida, tente de novo")
				continue
		if pecas[1]==pecas[2]==pecas[3]=="X" or pecas[4]==pecas[5]==pecas[6]=="X" or pecas[7]==pecas[8]==pecas[9]=="X" or pecas[1]==pecas[4]==pecas[7]=="X" or pecas[2]==pecas[5]==pecas[8]=="X" or pecas[3]==pecas[6]==pecas[9]=="X" or pecas[1]==pecas[5]==pecas[9]=="X" or pecas[3]==pecas[5]==pecas[7]=="X":
			print("----------FIM DE JOGO----------- \n  JOGADOR 1 VENCEU! \n")
			return False
		while turno(t)==2:
			j=int(input("\n Jogador 2, faça sua jogada, escolha a posição da sua peça O: "))
			if j>0 and j<10 and pecas[j]!="X" and pecas[j]!="O":
				pecas[j] = 'O' #substitui o número fornecido pelo jogador pela sua peca no tabuleiro
				t+=1
				continue
			else:
				print("Jogada invalida, tente de novo")
				continue
		if pecas[1]==pecas[2]==pecas[3]=="O" or pecas[4]==pecas[5]==pecas[6]=="O" or pecas[7]==pecas[8]==pecas[9]=="O" or pecas[1]==pecas[4]==pecas[7]=="O" or pecas[2]==pecas[5]==pecas[8]=="O" or pecas[3]==pecas[6]==pecas[9]=="O" or pecas[1]==pecas[5]==pecas[9]=="O" or pecas[3]==pecas[5]==pecas[7]=="O":
			print("----------FIM DE JOGO----------- \n JOGADOR 2 VENCEU! \n")
			return False 
		
