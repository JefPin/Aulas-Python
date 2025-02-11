import os
import random
os.system("clear||cls")

nomes = []

for i in range(10):
    nome = input(f"Digite o {i+1}º nome: ").lower()
    nomes.append(nome)

crush = random.choice(nomes)
os.system("clear||cls")

print(f"O nome do seu par ideal será: {crush.capitalize()}")

#while True:
#nomes = input("Digite um nome: ").lower()    