import os

os.system("cls || clear")

soma = 0
pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º Número: "))
    soma += numero

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

os.system("cls||clear")

print(f"Soma Total: {soma}")
print(f"Quantidade de Números Pares: {pares}")
print(f"Quantidade de Números Impares: {impares}")
