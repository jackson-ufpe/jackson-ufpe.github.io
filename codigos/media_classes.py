def criar_tabela(classes, frequencia):
    """
    Cria uma tabela a partir das classes e frequências fornecidas.

    Args:
        classes: Tupla de valores separados por espaços que representam as classes.
        frequencia: Lista de números decimais que representam as frequências.

    Returns:
        Uma string que representa a tabela formatada.
    """

    # Calcula o ponto médio (PM) de cada classe
    pm = [(float(classe.split()[0]) + float(classe.split()[1])) / 2 for classe in classes]

    # Calcula PM x f
    pm_f = [pm[i] * frequencia[i] for i in range(len(classes))]

    # Cria a tabela
    tabela = "Classes | Frequência | PM | PM x f\n"
    tabela += "------- | ----------- | --- | ------\n"
    for i in range(len(classes)):
        tabela += f"{classes[i]} | {frequencia[i]:.2f} | {pm[i]:.2f} | {pm_f[i]:.2f}\n"

    # Calcula e adiciona o somatório
    soma_frequencia = sum(frequencia)
    soma_pm_f = sum(pm_f)
    tabela += f"------- | ----------- | --- | ------\n"
    tabela += f"Total   | {soma_frequencia:.2f} |      | {soma_pm_f:.2f}\n"

    return tabela

# Inicializa listas para armazenar as classes e frequências
classes = []
frequencia = []

# Solicita as classes e frequências ao usuário, uma a uma
while True:
    classe = input("Digite a classe (ou 'f' para finalizar): ")
    if classe.lower() == 'f':
        break
    classes.append(classe)
    frequencia.append(float(input("Digite a frequência para a classe: ")))

# Cria e imprime a tabela
tabela = criar_tabela(classes, frequencia)
soma_pm_f = sum([(float(classe.split()[0]) + float(classe.split()[1])) / 2 * freq for classe, freq in zip(classes, frequencia)]) # Calculate soma_pm_f
soma_frequencia = sum(frequencia) # Calculate soma_frequencia
media = soma_pm_f / soma_frequencia # Calculate media
print(tabela)
print(f"Média ponderada: {media:.2f}")