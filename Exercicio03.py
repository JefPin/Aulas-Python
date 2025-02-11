import os 
import random
os.system("clear||cls")

sorteado = random.randint(1,100)
contador = 0

while True:
    numero = int(input("Digite um número de 1-100: "))
    contador = contador+1
    
    if(numero == sorteado):
        
        print(f"Parabéns, Você acertou o número em {contador} tentativas")
    elif(numero > sorteado):
        print("O número é menor!!")
    else:
        print("O número é maior!!")