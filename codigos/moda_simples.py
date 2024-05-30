import random

def calcular_moda(lista):
  """
  Calcula a moda de uma lista de números.

  Args:
    lista: Uma lista de números.

  Returns:
    Uma tupla contendo a moda e o tipo de distribuição modal.
  """
  contagem = {}
  for numero in lista:
    if numero in contagem:
      contagem[numero] += 1
    else:
      contagem[numero] = 1

  moda = []
  maior_contagem = 0
  for numero, contagem_numero in contagem.items():
    if contagem_numero > maior_contagem:
      moda = [numero]
      maior_contagem = contagem_numero
    elif contagem_numero == maior_contagem:
      moda.append(numero)

  if len(moda) == 1:
    distribuicao = "Distribuição modal"
  elif len(moda) == 2:
    distribuicao = "Distribuição bimodal"
  else:
    distribuicao = "Distribuição amodal"

  return moda, distribuicao

def obter_lista():
  """
  Obtém uma lista de números do usuário.

  Returns:
    Uma lista de números.
  """
  opcao = input("Como deseja inserir os dados? (1) Manualmente, (2) Separados por espaço, (3) Aleatórios: ")
  if opcao == '1':
    lista = []
    while True:
      numero = input("Digite um número (ou 'sair' para finalizar): ")
      if numero.lower() == 'sair':
        break
      try:
        lista.append(int(numero))
      except ValueError:
        print("Entrada inválida. Digite um número válido.")
    return lista
  elif opcao == '2':
    numeros = input("Digite os números separados por espaço: ")
    return [int(x) for x in numeros.split()]
  elif opcao == '3':
    tamanho = int(input("Digite o tamanho da lista aleatória: "))
    return random.sample(range(1, 100), tamanho)  # Gera números aleatórios de 1 a 99
  else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
    return obter_lista()

# Obter a lista de números
lista = obter_lista()

# Calcular a moda
moda, distribuicao = calcular_moda(lista)

# Imprimir os resultados
print("Lista:", lista)
print(f"{distribuicao}: {moda}")
