from corpo import corpo
def inicio():
    print("=====================================")
    print("************JOGO DA VELHA***************")
    print("=====================================")
    inicio = input(" \n 1- JOGAR \n 2- SAIR \n")
    if inicio == "1":
        print("--------COMEÇANDO O JOGO! --------")
        corpo()
    else:
        print("=============================================")
        quit()

if __name__=="__main__":
    inicio()
