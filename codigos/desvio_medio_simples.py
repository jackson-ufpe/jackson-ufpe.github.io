import random

def calcular_desvio_medio(lista):
  """Calcula o desvio médio de uma lista de números.

  Args:
    lista: Uma lista de números.

  Returns:
    O desvio médio da lista.
  """

  media = sum(lista) / len(lista)
  desvio_medio = sum(abs(x - media) for x in lista) / len(lista)
  return desvio_medio

def main():
  """Solicita ao usuário uma lista de números ou gera uma lista aleatória e calcula o desvio médio."""

  escolha = input("Deseja inserir uma lista de números ou gerar uma aleatória? (i/a): ")

  if escolha.lower() == 'i':
    numeros_str = input("Digite os números reais separados por espaço: ")
    numeros = [float(x) for x in numeros_str.split()]
  elif escolha.lower() == 'a':
    tamanho_lista = int(input("Digite o tamanho da lista aleatória: "))
    numeros = [random.uniform(0, 100) for _ in range(tamanho_lista)]
  else:
    print("Opção inválida. Por favor, digite 'i' para inserir ou 'a' para aleatório.")
    return

  desvio_medio = calcular_desvio_medio(numeros)
  #print(f"Quantidade de números {len(lista)}.")
  #print(f"Média geral: {media}.")
  print(f"O desvio médio da lista é: {desvio_medio}")

if __name__ == "__main__":
  main()
