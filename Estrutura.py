import os
os.system("clear||cls")

numeros = []

while True:
    valor = int(input("Digite um número: "))
    if(valor==-1):
        break
    else:
        numeros.append(valor)

for i in numeros:
    if(i%2==0):
        print(i)
    


#for i in range(len(numeros)):
    #print(numeros[i])

#for i in numeros:
    #print(i)