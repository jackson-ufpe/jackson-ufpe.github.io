import math
'''Cálculo da distribuição Poisson.'''

# Solicita as entradas do usuário
X = int(input("Digite o valor de X (número de ocorrências): "))
lambd = float(input("Digite o valor de λ (taxa média de ocorrências): "))

# Calcula a probabilidade usando a fórmula da distribuição de Poisson
probabilidade = (lambd**X * math.exp(-lambd)) / math.factorial(X)

# Imprime o resultado
print("A probabilidade de P(X) é:", probabilidade)
print("A probabilidade de P(X) é:", round(probabilidade * 100, 2))

