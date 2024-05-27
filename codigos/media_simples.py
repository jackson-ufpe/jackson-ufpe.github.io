import random

def calcular_media():
  """Calcula a média aritmética simples de uma lista de números."""

  while True:
    modo_insercao = input("Deseja inserir uma lista de números? (s/n): ").lower()
    if modo_insercao == 's':
      while True:
        try:
          numeros = input("Insira os números separados por espaço: ").split()
          numeros = [float(numero) for numero in numeros]
          break
        except ValueError:
          print("Entrada inválida. Por favor, insira números separados por espaço.")
      break
    elif modo_insercao == 'n':
      while True:
        modo_geracao = input("Deseja informar a lista de números manualmente ou criar aleatoriamente? (m/a): ").lower()
        if modo_geracao == 'm':
          while True:
            try:
              n = int(input("Quantos números deseja inserir? "))
              numeros = []
              for i in range(n):
                numero = float(input(f"Insira o {i+1} número: "))
                numeros.append(numero)
              break
            except ValueError:
              print("Entrada inválida. Por favor, insira um número inteiro.")
          break
        elif modo_geracao == 'a':
          while True:
            try:
              n = int(input("Quantos números aleatórios deseja gerar? "))
              numeros = [random.uniform(0, 100) for _ in range(n)]
              break
            except ValueError:
              print("Entrada inválida. Por favor, insira um número inteiro.")
          break
        else:
          print("Opção inválida. Por favor, escolha '(m)anual' ou '(a)leatorio'.")
      break
    else:
      print("Opção inválida. Por favor, digite 's' ou 'n'.")

  media = sum(numeros) / len(numeros)
  print(f"Lista de números: {numeros}")
  print(f"Quantidade de números: {len(numeros)}")
  print(f"Soma dos números: {sum(numeros, 2)}")
  print(f"A média aritmética simples da lista é: {round(media)}")

calcular_media()
