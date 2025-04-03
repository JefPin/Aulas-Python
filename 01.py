import os 
os.system("clear||cls")

peso_limite = 50  # Limite de peso em quilos
multa_por_quilo = 4.00  # Multa por quilo excedente

# Entrada do peso de peixes
total_peso = float(input("Digite o peso dos peixes em quilos: "))

# Cálculo do excesso e da multa
excesso = max(0, total_peso - peso_limite)
multa = excesso * multa_por_quilo

# Exibição dos resultados
print("\nResultado:")
print(f"Peso informado: {total_peso:.2f} kg")
print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")
