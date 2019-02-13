#!/usr/bin/env python3

import random

###############################################################################
################  CLASSE QUE REPRESENTA A PERSONAGEM PRINCIPAL ###############

class Personagem():
    
    def __init__(self,nome,classe,raça,HP,MP):
        self.nome = nome
        self.classe = classe
        self.raça=raça
        self.hpmax = HP
        self.mpmax = MP

    def __str__(self):
        return "{} é {} {}, com {}HP e {}MP, no nível {} e com {} de experiência".format(self.nome,self.raça,self.classe,self.hpmax,self.mpmax,self.nivel,self.xp)

    def atributos(self):
        """ Define atributos iniciais da personagem. Pretendo estabelcer o valor máximo em 50"""
        self.nivel=1
        self.xp=0
        self.força=float(random.randint(1,8))
        self.resistencia=float(random.randint(1,8))
        self.agilidade=float(random.randint(1,8))
        self.destreza=float(random.randint(1,8))
        self.inteligencia=float(random.randint(1,8))
        self.sagacidade=float(random.randint(1,8))
        self.vitalidade=float(random.randint(1,8)) 
        
        if self.raça=='Humano(a)':
            self.sagacidade += 3
            self.vitalidade += 1
            self.resistencia += 2
        elif self.raça=='Elfo(a)':
            self.agilidade += 3
            self.inteligencia += 2
            self.destreza += 2
        else:
            self.força += 3
            self.resistencia += 2
            self.vitalidade += 1


        if self.classe=='Guerreiro(a)':
            self.força += 5
            self.resistencia += 5
            self.vitalidade += 3
            
        elif self.classe=='Mago(a)':
            self.inteligencia += 5
            self.sagacidade += 5
            
        else:
            self.destreza += 5
            self.agilidade += 5
            self.sagacidade += 3
            
        self.ataque = self.força*2
        self.defesa = self.resistencia*2
        self.apmax = int(self.agilidade*(1.5))
        self.hpmax += self.vitalidade*2
        self.mpmax += self.inteligencia//2
        
        
    def ficha(self):
        """ Imprime uma ficha detalhada das características da personagem"""
        
        print("""
===============================================================================
  NOME: {:7}    RAÇA: {:9}   CLASSE: {:7}  NÍVEL: {:2}   XP: {}
  HP: {:4}   MP: {}  AP: {}
                                                      
FORÇA:        {:2}         ATAQUE: {:4}                             
RESISTÊNCIA:  {:2}         DEFESA: {:4}                             
AGILIDADE:    {:2}                                      
DESTREZA:     {:2}                                      
INTELIGÊNCIA: {:2}                                      
SAGACIDADE:   {:2}                                      
VITALIDADE:   {:2}                                      
================================================================================
""".format(self.nome, self.raça, self.classe, self.nivel, self.xp, self.hpmax,self.mpmax, self.apmax, self.força, self.ataque,self.resistencia, self.defesa,self.agilidade,self.destreza,self.inteligencia,self.sagacidade,self.vitalidade))

    def passou_de_nível(self):
        """ Calcula se a experiência total leva a personagem ao próximo nível """
        if self.xp >= 10^(self.nivel+1):
            self.nivel+=1
            return True
        else:
            return False

    def level_up(self): 
        """ 
        Função longa que implementa o Sistema de Passagem de Nível e atualiza Ataque, Defesa, HP, MP e AP 
        Cálculo: 1 vit => 2 HP
                 2 int => 1 MP
                 3 agi => 2 AP
                 1 for => 2 Ataque
                 1 res => 2 Defesa
        """
        confirmação={'F':'Força','f':'Força','R':'Resistência','r':'Resistência','D':'Destreza','d':'Destreza','A':'Agilidade','a':'Agilidade','I':'Inteligência','i':'Inteligência','S':'Sagacidade','s':'Sagacidade','V':'Vitalidade','v':'Vitalidade'}
        
        print("""================================================================================
================= PASSOU DE NÍVEL ! ============================================
              Você atingiu o nível {}!
Por isso você tem direito a 3 (três) pontos de atributos, apenas três(3). 
Não 4. Não 2... a não ser que coloque um terceiro depois. Mas 5 está fora de cogitação. 
Para alocar seus pontos, digite a primeira letra do atributo que deseja melhorar.""".format(self.nivel))
        
        for i in range(1,4):
            protagonista.ficha()
            melhoria = input("\nPonto {}: Qual atributo melhorar? ".format(i))
            confirma = input("\nConfirma melhoria de {}? (S/N)".format(confirmação[melhoria]))
            
            while confirma == 'n' or confirma == 'N':
                melhoria = input("\nPonto {}: Qual atributo melhorar? ".format(i))
                confirma = input("\nConfirma melhoria de {}? (S/N)".format(confirmação[melhoria]))
            
            if melhoria == 'F' or melhoria == 'f':
                self.força+=1
                self.ataque+=2
            elif melhoria=='R' or melhoria=='r':
                self.resistencia+=1
                self.defesa+=2
            elif melhoria=='A' or melhoria=='a':
                self.agilidade+=1
                self.apmax+=0.5
            elif melhoria=='D' or melhoria=='d':
                self.destreza+=1
            elif melhoria=='I' or melhoria=='i':
                self.inteligencia+=1
                self.mpmax+=0.5
            elif melhoria=='S' or melhoria=='s':
                self.sagacidade+=1
                self.descoberta+=3
            elif melhoria=='V' or melhoria=='v':
                self.vitalidade+=1
                self.hpmax+=2
            atributos = {'F':self.força,'f':self.força,'R':self.resistencia,'r':self.resistencia,'A':self.agilidade,'a':self.agilidade,'D':self.destreza,'d':self.destreza,'I':self.inteligencia,'i':self.inteligencia,'S':self.sagacidade,'s':self.sagacidade,'V':self.vitalidade,'v':self.vitalidade}
            print("\n Atualizado!  {} : {}".format(confirmação[melhoria],atributos[melhoria]))

################################### FIM DA CLASSE #######################################
#########################################################################################
#########################################################################################

############################ CRIAÇÃO DA  PERSONAGEM  ####################################

def escolhas_jogador():
    """
    Pergunta ao jogador as características gerais de sua personagem
    """
    dic_classes = {1:['Guerreiro(a)', 200, 0], 2:['Mago(a)', 100,100], 3:['Ladino(a)', 150,50]}
    dic_raças = {1:['Humano(a)',150,50],2:['Elfo(a)',100,100], 3:['Anão(ã)',200,0]}
    nome = input("\nQual o seu nome? ")
    
    classe = int(input("""
Escolha uma classe:
    (1) Guerreiro(a):
        Orgulham-se de sua Força e de sua Resistência. Muito poderosos em combates corpo-a-corpo,
        porém, em geral, não são muito espertos. Devido ao forte e intenso treinamento de combate,
        possuem muita Vitalidade e determinação.

    (2) Mago(a)
        Extremamente Inteligentes e Sagazes, magos são ótimos em imolar e pulverizar seus inimigos,
        devido ao seu arsenal de magias destruidoras. Se você pedir para um mago carregar uma caixa
        de laranjas, porém, coitado... ele nem a levanta do chão. 

    (3) Ladino(a)
        Ladrões e malandros, os ladinos são Ágeis e Destros, roubam qualquer coisa de qualquer um. 
        São Sagazes, pois a vida na rua os ensinou a sobreviver. Não são muito Fortes, mas sabem 
        se virar em todo tipo de combate.

>> Sua escolha: """))
    
    raça=int(input("""
Escolha uma raça:
    (1) Humano(a):
        São conhecidos por serem avarentos e maldosos por natureza. Possuem uma força de vontade 
        descomunal, porém apenas para se beneficiarem. Por isso, são bastante Sagazes e Resistentes,
        além de quererem Viver a todo custo. 

    (2) Elfo(a):
        Criaturas superiores que se acham divindades. São seres bastante esnobes, porém Inteligentes
        e Sagazes. São muito conhecidos por não de importarem com nada, apenas com o brilho de seus 
        cabelos e com o cheiro de suas roupas.

    (3) Anão(ã)
        Criaturas pequenas, atarracadas e rechondudas. São bastante teimosos, Fortes e Resistentes.
        Gostam de se vangloriar por construirem magníficos palácios sob montanhas recheados de ouro,
        mithril e pedras preciosas. Estudiosos dizem ser fruto do complexo de inferioridade. 

>> Sua escolha: """))
    
    return Personagem(nome, dic_classes[classe][0],dic_raças[raça][0],dic_classes[classe][1]+dic_raças[raça][1],dic_classes[classe][2]+dic_raças[raça][2])

def cria_personagem():
    """
    Termina de criar os atributos da personagem
    """
    protagonista = escolhas_jogador()
    protagonista.atributos()
    protagonista.ficha()
    rodar_de_novo=input("Rodar dados de atributos novamente? (S/N) ")
    while rodar_de_novo == "S" or rodar_de_novo=="s":
        protagonista.atributos()
        protagonista.ficha()
        rodar_de_novo=input("Rodar dados de atributos novamente? (S/N) ")
        if rodar_de_novo=="n" or rodar_de_novo=="N":
            break
    protagonista.ficha()

    return protagonista

###################################################################################################################################################

#### Cria personagens de monstros

class Goblin():

    def __init__(self,numero,nome,classe, nivel, exp_fornecida,hp,mp):
        self.numero=numero
        self.nome=nome
        self.classe=classe
        self.nivel = nivel
        self.exp_fornecida = exp_fornecida
        self.hpmax = hp
        self.mpmax = mp

    def __str__(self):
        return "Goblin {}".format(self.nome)#,self.nivel,self.hp,self.exp_fornecida)
        

    def atributos(self):
        if self.classe == 'Guerreiro':
            self.força = round(random.randint(1,4)*self.nivel*1.5, ndigits=1)
            self.resistencia = round(random.randint(1,4)*self.nivel*1.5,ndigits=1)
            self.agilidade =random.randint(1,4)*self.nivel
            self.destreza = random.randint(1,4)*self.nivel
            self.inteligencia = random.randint(1,4)
            self.sagacidade = random.randint(1,4)
            self.vitalidade = round(random.randint(1,4)*self.nivel*1.5,ndigits=1)
        elif self.classe == 'Ladrão':
            self.força = random.randint(1,4)*self.nivel
            self.resistencia = random.randint(1,4)
            self.agilidade = round(random.randint(1,4)*self.nivel*1.5,ndigits=1)
            self.destreza = round(random.randint(1,4)*self.nivel*1.5,ndigits=1)
            self.inteligencia = random.randint(1,4)
            self.sagacidade = random.randint(1,4)*self.nivel
            self.vitalidade = random.randint(1,4)
        self.ataque = self.força*2
        self.defesa = self.resistencia*2
        self.apmax = int(self.agilidade*(1.5))
        self.hpmax += self.vitalidade*2
        self.mpmax += self.inteligencia//2

    def ficha(self):
        """ Imprime uma ficha detalhada das características da personagem"""
        
        print("""
===============================================================================
  NOME: GOBLIN  CLASSE: {:7}  NÍVEL: {:2}   XP: {}
  HP: {:4}   MP: {}  AP: {}
                                                      
FORÇA:        {:2}         ATAQUE: {:4}                             
RESISTÊNCIA:  {:2}         DEFESA: {:4}                             
AGILIDADE:    {:2}                                      
DESTREZA:     {:2}                                      
INTELIGÊNCIA: {:2}                                      
SAGACIDADE:   {:2}                                      
VITALIDADE:   {:2}                                      
================================================================================
""".format(self.nome, self.nivel, self.exp_fornecida, self.hpmax,self.mpmax, self.apmax, self.força, self.ataque,self.resistencia, self.defesa,self.agilidade,self.destreza,self.inteligencia,self.sagacidade,self.vitalidade))




class Orc():
    pass


class Besta():
    pass





def cria_goblin(n ,nivel_max):
    """
    Cria n Goblins aleatórios (ou guerreiros ou ladrões) do nível 1 ao nivel_max
    """
    classes_de_goblins=['Guerreiro','Ladrão']
    grupo=[]
    for i in range(n):
        indice = random.randint(0,len(classes_de_goblins)-1)
        nivel_monstro=random.randint(1,nivel_max)
        exp = random.gauss((10**nivel_monstro)/2,2)

        if classes_de_goblins[indice]=='Guerreiro':
            hp = random.gauss((10**nivel_monstro)*random.randint(2,6),2)
            goblin=Goblin(i,"({}){}".format(str(i),classes_de_goblins[indice]),classes_de_goblins[indice],nivel_monstro,exp,hp,0)
        else:
            hp = random.gauss((10**nivel_monstro)*random.randint(2,4),2)
            mp=random.gauss((10**nivel_monstro)*random.randint(1,3),2)
            goblin=Goblin(i,"({}){}".format(str(i),classes_de_goblins[indice]),classes_de_goblins[indice], nivel_monstro,exp,hp,mp)
        goblin.atributos()
        grupo.append(goblin)
    return grupo

########################################################################
###################### SISTEMA DE COMBATE ##############################

def identifica_participantes(monstros_atacantes):
    """
    Função que toma uma lista de montros atacantes e retorna um dicionário com suas
    agilidades e nomes para conferir a ordem de ataque
    """
    dicionario =  {str(protagonista.agilidade):protagonista}
    for i in monstros_atacantes:
        #nome = "({}){}".format(str(i.numero),i.classe)
        dicionario[str(float(i.agilidade))]=i
    return dicionario


def verifica_agilidade(dict_agilidade):
    """
    Função que recebe o dicionário de agilidades e seleciona a maior agilidade do grupo
    Define quem ataca no momento
    """
    #if len(dict_agilidade.values())!=0:
    return str(max(list(map(float,dict_agilidade))))

    
def identifica_atacantes(monstros_vivos):
    """
    Função que recebe uma lista de monstros ainda vivos e retorna uma 
    cópia profunda como sendo uma lista de monstros aptos a atacar
    Essa lista sofrerá alterações a cada rodada assim que os monstros
    forem atacando
    """
    atacantes = []
    for i in range(monstros_vivos):
        atacantes.append(monstros_vivos[i])
    return atacantes


def menu_de_ataque(monstros_vivos):
    """
    Função que implementa um menu de escolhas ao 
    jogador durante seu turno de ataque
    """
    escolha = int(input("""
O que fazer?  

   (1) Atacar
   (2) Usar habilidade/magia
   (3) Usar item
   (4) Fugir

>> Sua escolha:  """))
    if escolha == 1:
        #Atacar
        for i in monstros_vivos:
            print(i,end='  ')
        print('\n')
        alvo = monstros_vivos[int(input("Escolha quem atacar: "))]
        ataque(alvo)
    #Usar habilidade/magia
    #Usar item
    #Fugir
    #Acessar ficha(?)

    pass


def habilidade():
    """
    Função que busca habilidades da protagonista e apresenta 
    para seleção do jogador e executa a função da habilidade
    """
    pass


def ataque(alvo):
    """
    Função que executa o ataque da protagonista
    em direção ao alvo escolhido
    """
    pass

def ataque_monstro(atacante):
    """
    Função que executa um ataque automático
    do monstro atacante à personagem protagonista
    """
    pass

def combate(monstros_vivos):
    """
    Implementa o Sistema de Combate, cujos passos são:
    -Indentificação dos participantes: quantos monstros há (lista fornecida)
    -Quem ataca primeiro? Verificação de Agilidade
    -Ataca quem? Menu de seleção com HP dos inimigos
    -Jogar dado de ataque/Jogar dado de defesa
    -Calcular e apresentar dano ou erro
    """

    HP = protagonista.hpmax
    MP = protagonista.mpmax
    monstros_atacantes = identifica_atacantes(monstros_vivos)
    # identificação dos participantes
    
    while HP>0:
        dicionario=identifica_participantes(monstros_atacantes)
        # Quem ataca primeiro?
        atacante = dicionario[verifica_agilidade(dicionario)]
        if atacante.nome == protagonista.nome:
            menu_de_ataque()
        else:
            ataque_monstro(atacante)
            
            
    
    
    
    



###########################################################################################
#################################### ÁREA DE TESTES #######################################
protagonista=cria_personagem()
monstros_vivos =  cria_goblin(3,3)
dicionario = identifica_participantes(monstros_vivos)
print(dicionario)
print(dicionario[verifica_agilidade(dicionario)])







#
# print("""
# -------------------------------------------------------------------
# Você não sabe onde está. Sabe que é uma floresta, mas não
# sabe qual. Sabe que está nela, mas não sabe como chegou
# ali. Andando sem rumo, você se vê de frente com uma cri-
# atura repugnante.
# """)
# grupo = cria_goblin(1,2)
# print(grupo[0])
# decisão=int(input("""

# Você luta(1) ou foge(2)? 
# """))
# if decisão == 1:
#     while protagonista.hp > 0:
#         dado1 = random.randint(1,20)
#         dado2 = random.randint(1,20)
#         if protagonista.ap > grupo[0].ap:
#             if dado1+protagonista.destreza > 15+grupo[0].sagacidade:
#                 if dado2+grupo[0].sagacidade > 15:
#                     grupo[0].hp -= protagonista.ataque - grupo[0].defesa
#                 else:
#                     grupo[0].hp -= protagonista.ataque
#             else:
#                 print("Você errou o golpe!")
#             dado1 = random.randint(1,20)
#             dado2 = random.randint(1,20)
#             if dado1+grupo[0].destreza > 15+protagonista.sagacidade:
#                 if dado2+protagonista.sagacidade > 15:
#                     protagonista.hp -= grupo[0].ataque - protagonista.defesa
#                 else:
#                     protagonista.hp -= grupo[0].ataque
#             else:
#                 print("O monstro errou o golpe!")

    
#         else:
#             if dado1+grupo[0].destreza > 15+protagonista.sagacidade:
#                 if dado2+protagonista.sagacidade > 15:
#                     protagonista.hp -= grupo[0].ataque - protagonista.defesa
#                 else:
#                     protagonista.hp -= grupo[0].ataque
#             else:
#                 print("O monstro errou o golpe!")
#             dado1 = random.randint(1,20)
#             dado2 = random.randint(1,20)
            
#             if dado1+protagonista.destreza > 15+grupo[0].sagacidade:
#                 if dado2+grupo[0].sagacidade > 15:
#                     grupo[0].hp -= protagonista.ataque - grupo[0].defesa
#                 else:
#                     grupo[0].hp -= protagonista.ataque
#             else:
#                 print("Você errou o golpe!")
#         if grupo[0].hp <= 0:
#             print("\n O Goblin está morto e você sobreviveu!")
#             protagonista.xp += grupo[0].exp_fornecida
#             break
#     if protagonista.hp <=0:
#         print("Você morreu e o Goblin está rindo da sua cara!")
# else:
#     fuga = randon.randint(1,20)
#     if fuga > 15:
#         print("Você escapou!")
#     else:
#         print("Você morreu e o Goblin está rindo da sua cara!")
# if protagonista.passou_de_nível():
#     protagonista.level_up()
# protagonista.ficha()
# 
#############################################################################################

    
    
###################################################################
###################### ORGANIZANDO O JOGO #########################

############### ROGUE-LIKE PYTHON GAME (RPG) ######################

# Criação de Personagem protagonista


# Contextualização: texto apresentando a situação da protagonista


# Menu de ações: #Gerenciar itens
                 #Acssar ficha
                 #Usar habilidade/magia
                 #Abrir porta

# Menu de Combate: #Acessar ficha
                   #Atacar
                   #Usar habilidade/magia
                   #Usar item
                   #Visualizar inimigos
                   #Fugir


# Verificar experiência -> passagem de nível

# Menu de ações

###### COMBATE FINAL: MONSTRO ESPECIAL! ########


