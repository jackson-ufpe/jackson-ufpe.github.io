def calcular_md():
  """
  Calcula o valor de Md usando a fórmula fornecida,
  solicitando os dados do usuário.
  """

  li = float(input("Insira o valor de Li: "))
  n = float(input("Insira o valor de N: "))
  soma_f_ant = float(input("Insira a soma dos valores de f_ant: "))
  f_md = float(input("Insira o valor de f_md: "))

  md = li + ((n / 2 - soma_f_ant) / f_md)
  print(f"Md = {md}")

# Chama a função para calcular Md
calcular_md()