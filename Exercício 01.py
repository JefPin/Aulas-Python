import os

os.system("cls || clear")

primeiroValor = int(input("Digite o Primeiro Número: "))
segundoValor = int(input("Digite o Segundo Número: "))

soma = primeiroValor + segundoValor
media = soma/2
multi = primeiroValor * segundoValor

# caso seja tenha mais Valores.

# menor = min(primeiroValor, segundoValor)
# maior = max(primeiroValor, segundoValor)

if primeiroValor > segundoValor:
    print("O 1º Número é maior que o 2º.")
elif primeiroValor == segundoValor:
    print("Números iguais.") 
else:
    print("O 2º Número é Maior que o 1º Número. \n")       

print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {multi}")

# print(f"Menor valor: {menor}")
# print(f"Maior Valor {maior}")
