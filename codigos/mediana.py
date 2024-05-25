def calcular_mediana(numeros):
  """Calcula a mediana de uma lista de números.

  Args:
    numeros: Uma lista de números.

  Returns:
    A mediana da lista de números.
  """
  numeros.sort()
  n = len(numeros)
  meio = n // 2
  if n % 2 == 0:
    # Se o número de elementos for par, a mediana é a média dos dois elementos do meio
    mediana = (numeros[meio - 1] + numeros[meio]) / 2
  else:
    # Se o número de elementos for ímpar, a mediana é o elemento do meio
    mediana = numeros[meio]
  return mediana

# Obter a entrada do usuário
entrada = input("Digite uma série de números separados por espaços: ")

# Dividir a entrada em uma lista de números
numeros = [float(x) for x in entrada.split()]

# Calcular e imprimir a mediana
mediana = calcular_mediana(numeros)
print(f"Lista de números: {numeros}")
print(f"Quantidade de números: {len(numeros)}")
print(f"A mediana da série é: {mediana}")