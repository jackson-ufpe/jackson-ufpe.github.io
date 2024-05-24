import random
import math
from collections import Counter

def calcular_frequencia(dados, amplitude_classe):
  """Calcula a frequência absoluta, acumulada e relativa de uma lista de dados, agrupados em classes.

  Args:
    dados: Uma lista de dados.
    amplitude_classe: A amplitude de cada classe.

  Returns:
    Um dicionário com a frequência absoluta, acumulada e relativa de cada classe.
  """
  menor_valor = min(dados)
  maior_valor = max(dados)
  limite_inferior = menor_valor
  limite_superior = limite_inferior + amplitude_classe

  classes = {}
  frequencia = {}
  frequencia_acumulada = {}
  frequencia_relativa = {}
  acumulada = 0

  while limite_inferior < maior_valor:
    classe = (limite_inferior, limite_superior)
    classes[classe] = 0

    for dado in dados:
      if limite_inferior <= dado < limite_superior:
        classes[classe] += 1

    frequencia[classe] = classes[classe]
    acumulada += classes[classe]
    frequencia_acumulada[classe] = acumulada
    frequencia_relativa[classe] = classes[classe] / len(dados)

    limite_inferior = limite_superior
    limite_superior += amplitude_classe

  return frequencia, frequencia_acumulada, frequencia_relativa

def imprimir_tabela(frequencia, frequencia_acumulada, frequencia_relativa):
  """Imprime a tabela de frequência com classes, frequências absoluta, acumulada e relativa.

  Args:
    frequencia: Um dicionário com a frequência absoluta de cada classe.
    frequencia_acumulada: Um dicionário com a frequência acumulada de cada classe.
    frequencia_relativa: Um dicionário com a frequência relativa de cada classe.
  """
  print("-" * 70)
  print(f"{'Classe':<15} | {'Frequência Absoluta':<20} | {'Frequência Acumulada':<20} | {'Frequência Relativa':<20}")
  print("-" * 70)
  for classe in sorted(frequencia.keys()):
    freq = frequencia[classe]
    freq_ac = frequencia_acumulada[classe]
    print(f"{classe[0]:.2f} - {classe[1]:.2f} | {freq:<20} | {freq_ac:<20} | {frequencia_relativa[classe]:<20.2%}")
  total_frequencia = sum(frequencia.values())
  print("-" * 70)
  print(f"{'Total':<15} | {total_frequencia:<20}")
  print("-" * 70)

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
    quantidade = len(numeros)  # Define quantidade após ler a lista
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
        numero = random.uniform(1, 100)  # Gera números aleatórios entre 1 e 100
        numeros.append(numero)
    else:
      print("Opção inválida. Encerrando o programa.")
      return
  else:
    print("Opção inválida. Encerrando o programa.")
    return

  amplitude_total = (max(numeros) + min(numeros)) / 2
  numero_classes = int(math.sqrt(quantidade))
  amplitude_classe = int(amplitude_total / numero_classes)
  if amplitude_classe < 1:
    amplitude_classe = 1

  frequencia, frequencia_acumulada, frequencia_relativa = calcular_frequencia(numeros, amplitude_classe)
  imprimir_tabela(frequencia, frequencia_acumulada, frequencia_relativa)

if __name__ == "__main__":
  main()