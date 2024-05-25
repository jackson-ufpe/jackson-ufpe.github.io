def calcular_mo():
  """
  Calcula o valor de Mo usando a fórmula fornecida,
  solicitando os dados do usuário.
  """

  li = float(input("Insira o valor de Li: "))
  f_post = float(input("Insira o valor de f_post: "))
  a = float(input("Insira o valor de A: "))
  f_ant = float(input("Insira o valor de f_ant: "))

  mo = li + ((f_post * a) / (f_ant + f_post))
  print(f"Mo = {mo}")

# Chama a função para calcular Mo
calcular_mo()