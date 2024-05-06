# Recebe o salário atual do colaborador
salario_atual = float(input("Digite o salário atual do colaborador: "))

# Calcula o reajuste de acordo com as faixas salariais definidas
if salario_atual <= 280.00:
    percentual_aumento = 20
elif salario_atual >= 280.00 and salario_atual < 700.00:
    percentual_aumento = 15
elif salario_atual >= 700.00 and salario_atual < 1500.00:
    percentual_aumento = 10
elif salario_atual >= 1500.00: 
    percentual_aumento = 5

# Calcula o valor do aumento e o novo salário
valor_aumento = salario_atual * percentual_aumento / 100
novo_salario = salario_atual + valor_aumento

# Exibe os resultados
print("\nSalário antes do reajuste:", salario_atual)
print("Percentual de aumento aplicado:", percentual_aumento, "%")
print("Valor do aumento:", valor_aumento)
print("Novo salário após o reajuste:", novo_salario)