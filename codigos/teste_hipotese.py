import math

# Solicita as entradas do usuário
# a = float(input("Nível de significância (em %): "))

# Calcula nível de significância para encontrar o valor de Z na tabela de distribuição normal
# ns = 0.5 - a
# print(ns)

# Solicita mais entradas do usuário
X = float(input("Média amostral (X): "))
u = float(input("Média populacional (u): "))
s = float(input("Desvio padrão (S): "))
N = float(input("Numero total da amostra (N): "))

# Calcula o valor de estimador
estimador = (X - u) / (s / math.sqrt(N))

# Imprime o resultado
print(f"Estimador: {round(estimador, 2)}")
print("Compare com o valor de Z para aceitar ou rejeitar a hipótese nula.")