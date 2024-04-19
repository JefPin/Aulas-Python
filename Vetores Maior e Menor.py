import os 

os.system("clear")

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

    maiorNumero = max(numeros)
    menorNumero = min(numeros)

print(f"\nMaior Número: {maiorNumero}")
print(f"Menor Número: {menorNumero}")
