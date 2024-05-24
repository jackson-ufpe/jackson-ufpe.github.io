# Solicita ao usuário uma lista de números separados por espaço
entrada = input("Digite uma lista de números separados por espaço: ")

# Converte a entrada do usuário em uma lista de números
lista_informada = [int(numero) for numero in entrada.split()]

# Ordena a lista de números em ordem crescente
lista_ordenada = sorted(lista_informada)

# Exibe a lista ordenada
print()
print("Tamanho da lista informada:", len(lista_informada))
print("A lista ordenada é:", lista_ordenada)