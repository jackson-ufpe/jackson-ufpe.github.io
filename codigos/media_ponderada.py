import random

def calcular_media_ponderada():
  """Calcula a média ponderada de uma lista de números com seus respectivos pesos."""
  while True:
    modo_insercao = input("Deseja inserir uma lista de números? (s/n): ").lower()
    if modo_insercao == 's':
      while True:
        try:
          numeros_str = input("Insira os números separados por espaço: ").split()
          pesos_str = input("Insira os pesos correspondentes separados por espaço: ").split()
          numeros = [float(numero) for numero in numeros_str]
          pesos = [float(peso) for peso in pesos_str]
          if len(numeros) != len(pesos):
            print("O número de números e pesos deve ser igual.")
          else:
            break
        except ValueError:
          print("Entrada inválida. Por favor, insira números válidos separados por espaço.")
      break
    elif modo_insercao == 'n':
      while True:
        modo_geracao = input("Deseja informar a lista de números manualmente ou criar aleatoriamente? (m/a): ").lower()
        if modo_geracao == 'm':
          while True:
            try:
              n = int(input("Quantos números deseja inserir? "))
              numeros = []
              pesos = []
              for i in range(n):
                numero = float(input(f"Insira o {i+1} número: "))
                peso = float(input(f"Insira o peso do {i+1} número: "))
                numeros.append(numero)
                pesos.append(peso)
              break
            except ValueError:
              print("Entrada inválida. Por favor, insira números válidos.")
          break
        elif modo_geracao == 'a':
          while True:
            try:
              n = int(input("Quantos números aleatórios deseja gerar? "))
              numeros = [random.uniform(0, 100) for _ in range(n)]
              pesos = [random.randint(1, 5) for _ in range(n)]
              break
            except ValueError:
              print("Entrada inválida. Por favor, insira um número inteiro.")
          break
        else:
          print("Opção inválida. Por favor, escolha 'manual' ou 'aleatorio'.")
      break
    else:
      print("Opção inválida. Por favor, digite 's' ou 'n'.")

  soma_ponderada = sum([numeros[i] * pesos[i] for i in range(len(numeros))])
  soma_pesos = sum(pesos)
  media_ponderada = soma_ponderada / soma_pesos

  # Exibir dados em formato de tabela
  print("-" * 40)
  print("Dados Informados | Frequência | Dados x F")
  print("-" * 40)
  for i in range(len(numeros)):
    print(f"{numeros[i]:15.2f} | {pesos[i]:10.2f} | {numeros[i] * pesos[i]:10.2f}")
  print("-" * 40)
  print(f"Total:          | {soma_pesos:10.2f} | {soma_ponderada:10.2f}")
  print("-" * 40)

  print(f"Quantidade de números: {len(numeros)}")
  print(f"A média ponderada da lista é: {media_ponderada}")

calcular_media_ponderada()