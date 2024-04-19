import os 

os.system("cls || clear")

notas = []
soma = 0.0
media = 0.0

for i in range(4):
    nota = float(input(f"Digite sua {i+1}ª Nota: "))
    notas.append(nota)

    soma += notas[i]
media = soma/len(notas)

print(f"\nMédia: {media}")

if (media >= 7):
    print("Aprovado.")
elif (media >= 5):
    print("Recuperação.")
else:
    print("Reprovado.")    
