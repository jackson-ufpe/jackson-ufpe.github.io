def calcular_media_ponderada():
  """Calcula a média ponderada de uma lista de números com pesos baseados na frequência e exibe os dados em uma tabela com somas."""

  while True:
    modo_insercao = input("Deseja inserir uma lista de números? (sim/não): ").lower()
    if modo_insercao == 'sim':
      while True:
        try:
          numeros_str = input("Insira os números separados por espaço: ").split()
          numeros = [float(numero) for numero in numeros_str]
          break
        except ValueError:
          print("Entrada inválida. Por favor, insira números válidos separados por espaço.")
      break
    elif modo_insercao == 'não':
      while True:
        modo_geracao = input("Deseja informar a lista de números manualmente ou criar aleatoriamente? (manual/aleatorio): ").lower()
        if modo_geracao == 'manual':
          while True:
            try:
              n = int(input("Quantos números deseja inserir? "))
              numeros = []
              for i in range(n):
                numero = float(input(f"Insira o {i+1}º número: "))
                numeros.append(numero)
              break
            except ValueError:
              print("Entrada inválida. Por favor, insira um número válido.")
          break
        elif modo_geracao == 'aleatorio':
          while True:
            try:
              n = int(input("Quantos números aleatórios deseja gerar? "))
              numeros = [random.uniform(0, 100) for _ in range(n)]
              break
            except ValueError:
              print("Entrada inválida. Por favor, insira um número inteiro.")
          break
        else:
          print("Opção inválida. Por favor, escolha 'manual' ou 'aleatorio'.")
      break
    else:
      print("Opção inválida. Por favor, digite 'sim' ou 'não'.")

  # Calcula a frequência de cada número
  frequencias = {}
  for numero in numeros:
    if numero in frequencias:
      frequencias[numero] += 1
    else:
      frequencias[numero] = 1

  # Calcula a média ponderada
  soma_ponderada = 0
  soma_pesos = 0
  for numero, frequencia in frequencias.items():
    soma_ponderada += numero * frequencia
    soma_pesos += frequencia

  media_ponderada = soma_ponderada / soma_pesos

  # Imprime os dados em uma tabela
  print("-" * 40)
  print(f"| {'Dados Informados':^15} | {'Frequência':^10} | {'Dados x F':^15} |")
  print("-" * 40)
  soma_dados = 0
  soma_frequencias = 0
  soma_produto = 0
  for numero, frequencia in frequencias.items():
    print(f"| {numero:^15.2f} | {frequencia:^10} | {numero * frequencia:^15.2f} |")
    soma_dados += numero
    soma_frequencias += frequencia
    soma_produto += numero * frequencia
  print("-" * 40)
  print(f"| {soma_dados:^15.2f} | {soma_frequencias:^10} | {soma_produto:^15.2f} |")
  print("-" * 40)
  print(f"Média Ponderada: {media_ponderada:.2f}")

calcular_media_ponderada()

*****

def calcular_media_ponderada():
  """Calcula a média ponderada de uma lista de números com pesos baseados na frequência."""

  while True:
    modo_insercao = input("Deseja inserir uma lista de números? (s/n): ").lower()
    if modo_insercao == 's':
      while True:
        try:
          numeros_str = input("Insira os números separados por espaço: ").split()
          numeros = [float(numero) for numero in numeros_str]
          break
        except ValueError:
          print("Entrada inválida. Por favor, insira números válidos separados por espaço.")
      break
    elif modo_insercao == 'n':
      while True:
        modo_geracao = input("Deseja informar a lista de números manualmente ou criar aleatoriamente? (ma/a): ").lower()
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
              print("Entrada inválida. Por favor, insira um número válido.")
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
          print("Opção inválida. Por favor, escolha 'manual' ou 'aleatorio'.")
      break
    else:
      print("Opção inválida. Por favor, digite 's' ou 'n'.")

  # Calcula a frequência de cada número
  frequencias = {}
  for numero in numeros:
    if numero in frequencias:
      frequencias[numero] += 1
    else:
      frequencias[numero] = 1

  # Calcula a média ponderada
  soma_ponderada = 0
  soma_pesos = 0
  for numero, frequencia in frequencias.items():
    soma_ponderada += numero * frequencia
    soma_pesos += frequencia

  media_ponderada = soma_ponderada / soma_pesos
  print(f"Lista de números: {numeros}")
  print(f"Quantidade de números: {len(numeros)}")
  print(f"Frequência de cada número: {frequencias}")
  print(f"A média ponderada da lista é: {media_ponderada}")

calcular_media_ponderada()