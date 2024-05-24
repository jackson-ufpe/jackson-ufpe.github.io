import math
'''Cálculo de distribuição binomial'''

# Solicita as entradas do usuário
N = int(input("Digite o valor de N (número total de ensaios): "))
X = int(input("Digite o valor de X (número de sucessos): "))
p = float(input("Digite o valor de p (probabilidade de sucesso em um único ensaio em %): "))

# Calcula e exibe q (probabilidade de falha)
q = 1 - p
print("O valor de q:", q)

# Calcula a probabilidade usando a fórmula da distribuição binomial
probabilidade = (math.factorial(N) / (math.factorial(X) * math.factorial(N - X))) * (p**X) * (q**(N - X))

# Imprime o resultado
print("A probabilidade de P(X) sem formatar:", probabilidade)
print("A probabilidade de P(X) arredondada:", round(probabilidade * 100, 2))

