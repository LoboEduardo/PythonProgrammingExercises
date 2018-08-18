#!/usr/bin/env python3
def primo(n):
    '''Função que verifica se um número n é primo'''
    é_primo = True   
    while é_primo:
        for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    é_primo = False
        break                
    return é_primo
        






def soma():
    '''função para verificar se um número é a soma de dois primos
A estratégia é subtrair do número dado um número primo e verificar se
o resultado também é primo'''

    print("""   Função para verificar se um número é a soma de dois primos
   A estratégia é subtrair do número dado um número primo e verificar se
   o resultado também é primo \n""")

    
    num = int(input("\n Digite um número inteiro e positivo: "))
    while num<=0:
        num = int(input("\n Número inválido . \n Digite um número inteiro e positivo: "))

    não_é_soma = True  #partindo do princípio de que num é uma soma de dois primos

    # já tratando do caso especial dos números 1,2,3
    #como 1 não é primo, 2 não é soma de dois primos
    # pelo mesmo motivo, 3 não é soma de dois primos
    if num ==1 or num ==2 or num ==3:
            não_é_soma = True
    
    # caso o número não seja 1 ou 2 ou 3
    while não_é_soma:
        for i in range(2,(int(num**0.5)+1)):
            if primo(i)==False:
                continue
            else:
                print(i)
                if primo(num - i):
                    não_é_soma=False
                    break
                else:
                    continue
        break
    #print("{}  |  {}".format(i, num-i))
    
    if não_é_soma:
        print("{} não é a soma de dois primos".format(num))
    else:
        print("{} é a soma dos primos {} e {}".format(num, i, num-i))




if __name__ == "__main__":
    soma()
        
              
