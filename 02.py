salario_atual = float(input("Digite o salário atual do colaborador: "))

if salario_atual <= 280:
    percentual = 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

# Cálculo do aumento e novo salário
aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + aumento

# Exibição dos resultados
print("\nResultado do Reajuste Salarial:")
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
