import os

os.system("clear")

nota = 11.0
soma = 0.0
media = 0.0

while nota < 0 or nota > 10:
    for i in range(0,2):
        nota = float(input(f"Digite sua {i+1}ª Nota: "))
        
    
        if nota > 0 or nota < 10:
            soma += nota
            
media = soma /2
    
print(f"Média do Aluno: {media}")
    
