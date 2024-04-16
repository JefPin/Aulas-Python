import os

os.system("clear")

# Dinâmico.
nome = input("Digite seu nome: ")

# Estática.
idade: int 
idade = int(input("Digite seu nome: "))

# Exibindo dados.
print(f"Nomes: {nome}")
print(f"Idade: {idade}")

# Condicionais if.

if idade >= 65:
    print("Requerer a Aposentadoria.")
else:
    print("Não Requerer a Aposentadoria.")

# Condicionais While.    
numero = 1    
    
while numero <= 10:
    print(numero)
    numero+= 1
    
