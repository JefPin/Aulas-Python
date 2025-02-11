import os
os.system("clear||cls")

nomes = []

while True:
    nome = input("Digite um nome: ").lower()
    if(nome=='exit'):
        break
    else:
        nomes.append(nome)
    
for i in nomes:
    if(i.startswith('a')):
        print(i.capitalize())