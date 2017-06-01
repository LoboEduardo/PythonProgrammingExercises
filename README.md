num=int(input("Vamos achar os divisores do número: "))
div=[]
for x in range(1,num):
    if num%x==0:
        div.append(x)
print("Os divisores de ",num, "são: ", div)
