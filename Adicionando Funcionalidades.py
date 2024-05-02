import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calculoIMC(peso,altura):
    imcs = 0.0
    imcs = (peso / (altura * altura)) 
    return imcs
    
def i_m_c():
    if imc[i] <= 18.5:
        print("Abaixo do Peso\n")
    elif imc[i] >= 18.5 and imc[i] < 25:    
        print("Peso Normal\n")
    elif imc[i] >= 25 and imc[i] < 30:
        print("Sobrepeso\n")
    elif imc[i] >= 30 and imc[i] < 35:
        print("Obesidade Grau I\n")
    elif imc[i] >= 35 and imc[i] < 40:
        print("Obesidade Grau II\n")
    elif imc[i] >= 40:
        print("Obesidade Grau III (Mórbida)\n")
        
    
# Definindo listas vazias para armazenar os dados dos usuários

imcs = 0.0
imc = []
Sobrenomes = []
nomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite seu Sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))

    # Adicionando os dados às listas
    imcs = calculoIMC(peso,altura)
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    Sobrenomes.append(sobrenome)
    imc.append(imcs)
    
    
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], Sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC: {imc[i]:.1f}")
    i_m_c()
  
