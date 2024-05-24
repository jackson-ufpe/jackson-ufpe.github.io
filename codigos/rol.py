import random
from collections import Counter

def calcular_frequencia(dados):
  """Calcula a frequência absoluta, acumulada e relativa de uma lista de dados.

  Args:
    dados: Uma lista de dados.

  Returns:
    Um dicionário com a frequência absoluta, acumulada e relativa de cada dado.
  """
  total = len(dados)
  frequencia = Counter(dados)
  frequencia_relativa = {k: v / total for k, v in frequencia.items()}
  frequencia_acumulada = {}
  acumulada = 0
  for dado, freq in sorted(frequencia.items()):
    acumulada += freq
    frequencia_acumulada[dado] = acumulada
  return frequencia, frequencia_acumulada, frequencia_relativa

def imprimir_tabela(frequencia, frequencia_acumulada, frequencia_relativa):
  """Imprime a tabela de frequência absoluta, acumulada e relativa, ordenada pelos dados.

  Args:
    frequencia: Um dicionário com a frequência absoluta de cada dado.
    frequencia_acumulada: Um dicionário com a frequência acumulada de cada dado.
    frequencia_relativa: Um dicionário com a frequência relativa de cada dado.
  """
  print("-" * 50)
  print(f"{'Dado':<10} | {'Frequência Absoluta':<20} | {'Frequência Acumulada':<20} | {'Frequência Relativa':<20}")
  print("-" * 50)
  dados_ordenados = sorted(frequencia.keys())
  for dado in dados_ordenados:
    freq = frequencia[dado]
    freq_ac = frequencia_acumulada[dado]
    print(f"{dado:<10.2f} | {freq:<20} | {freq_ac:<20} | {frequencia_relativa[dado]:<20.2%}")
  total_frequencia = sum(frequencia.values())
  print("-" * 50)
  print(f"{'Total':<10} | {total_frequencia:<20}")
  print("-" * 50)

def main():
  """Recebe os dados do usuário, calcula e imprime a tabela de frequência."""

  numeros = []

  escolha_lista = input("Deseja inserir uma lista de números separados por espaço? (S/N): ").upper()

  if escolha_lista == 'S':
    lista_str = input("Digite a lista de números separados por espaço: ")
    try:
      numeros = [float(numero.strip()) for numero in lista_str.split()]
    except ValueError:
      print("Lista inválida. Certifique-se de inserir números separados por espaço.")
      return
  elif escolha_lista == 'N':
    quantidade = int(input("Informe a quantidade de números: "))
    escolha_entrada = input("Deseja informar os números (I) ou gerá-los aleatoriamente (A)? ").upper()

    if escolha_entrada == 'I':
      for i in range(quantidade):
        while True:
          try:
            numero = float(input(f"Informe o {i+1}º número: "))
            numeros.append(numero)
            break
          except ValueError:
            print("Valor inválido. Insira um número inteiro ou decimal.")
    elif escolha_entrada == 'A':
      for _ in range(quantidade):
        numero = random.uniform(1, 100)
        numeros.append(numero)
    else:
      print("Opção inválida. Encerrando o programa.")
      return
  else:
    print("Opção inválida. Encerrando o programa.")
    return

  frequencia, frequencia_acumulada, frequencia_relativa = calcular_frequencia(numeros)
  imprimir_tabela(frequencia, frequencia_acumulada, frequencia_relativa)

if __name__ == "__main__":
  main()