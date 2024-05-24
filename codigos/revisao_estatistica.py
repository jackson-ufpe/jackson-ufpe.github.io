import streamlit as st


def inicio():
    import streamlit as st

    st.write("# Revisão de estatística.")
    st.sidebar.success("Navegue pelos tópicos.")

    st.markdown(
        """
        ## Notas de aula...

        Anotações resumidas da disciplina de estatística.
        
        Navegue pelos tópicos ao lado para acessar os conteúdos.

        Alguns códigos disponíveis neste repositório [GitHub](#)
    """
)


def introducao():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(paginas.keys())[1]}")
    st.write(
        """
        ## Conceitos

        **Estatística**, processamento (organização, análise e interpretação) de dados para gerar (apresentar) informações para tomadas de decisões assertivas.

        Estatística descritiva (descrição) e indutiva (inferências a partir de população e amostra).

        População, amostra, estatística descritiva (tabelas, gráficos, medidas), características amostrais, estatística indutiva, características populacionais (inferências).

        Fases do método estatístico: definição do problema, delimitação do problema, planejamento, coleta de dados, apuração de dados, apresentação de dados, análise de dados, interpretação de dados.

        ### Variáveis

        **Qualitativas** (qualidades ou atributos, nominais ou ordinais [ordem]) e **quantitativas** (quantidade, discretas [contagens], contínuas [medidas]).

        ### Distribuição e frequência

        **Rol** (ordenação) contar (frequência [absoluta (f)] de repetição).
        Frequência acumulada (soma das frequências) e frequência relativa (fr) (divisão da frequência absoluta (f) pelo número de elementos (N) da amostra, em percentual).

        ### Distribuição e frequência por classe

        **Classe (faixa de valor)** com limites inferiores e superiores, amplitude (A = Ls - Li) invariável, ponto médio (Pm = Ls + Li) / 2) variável.

        ### Séries e gráficos

        **Séries** temporais, geográficas, categóricas ou específicas, mistas.
        Gráficos de linhas (tempo), barras (tempo), pizza (setor, percentual), coluna (comparações), histograma (distribuição de frequência por classe)...
    """
)


def medidas_posicao():
    import streamlit as st

    st.markdown(f"# {list(paginas.keys())[2]}")
    st.write(
        """
        **Medidas de posição (tendência central)**, média, mediana e moda.

        **Média**, quociente entre a soma de todos os valores da variável e seu número de elementos. Fórmula: X barra igual ao somatório de X sobre N.

        **Média ponderada** (distribuição de frequência), quociente entre a soma de todos os valores da variável multiplicados por suas frequências (pesos) e seu número de elementos. Fórmula: X barra igual ao somatório da multiplicação de X por sua respectiva frequência (f) sobre N.

        **Mediana**, valor que divide a série em dois conjuntos de igual tamanho. Se o número de dados for ímpar, a mediana está no centro, se for par, a mediana é a média aritmética dos dois valores no centro da série.

        **Moda**, valor de maior frequência.

        #### Tipos:

        **Distribuição modal**, apenas um valor.

        **Distribuição bimodal**, dois ou mais valores,
        
        **Distribuição amodal**, sem moda.

        #### Exemplos:
    """
)

    st.latex(r'''        
        \textbf{Média aritmética simples }
            
            \bar{x} = \frac{2 + 5 + 9 + 1 + 7}{5} = 4.8
    '''
    )

    st.latex(r'''        
        \textbf{Média ponderada }
            
            \bar{x}_w = \frac{(2 \times 5) + (7 \times 3) + (4 \times 2) + (9 \times 4)}{(5 + 3 + 2 + 4)} = 5.21
    '''
    )

def medidas_dispersao():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(paginas.keys())[3]}")
    st.write(
        """
        **Medidas de dispersão**, medidas para verificar o quanto os valores estão afastados em relação a média.

        **Amplitude total**, diferença entre o maior e o menor valor da série. Quanto maior a amplitude, maior a dispersão.

        **Desvio médio**, a média das distâncias entre cada elemento da amosta e seu valor médio.

        **Variância**, média dos quadrados dos desvios. Desvios proporcionais as dispersões.

        **Assimetria**, grau de afastamento de uma distribuição da unidade de simetria. 

        #### Tipos:

        **Simétrica**, igualdade dos valores de média, mediana e moda.
        
        **Assimétrica a direita**, ...
    """
)


def probabilidade():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(paginas.keys())[4]}")
    st.write(
        """
        **Probabilidade**, possibilidade (medida de grau de incerteza) de ocorrência de um determinado evento definido num espaço amostral relacionado a um evento aleatório.

        **Experimento aleatório (E)**, imprevisíveis.

        **Espaço amostral (S)**, conjunto de todos os resultados possíveis do evento estatístico.

        **Cálculo da probabilidade**, número de elementos do evento A sobre o número de elementos do espaço amostral S, P(A)=A/S; A sempre menor ou igual a S.

        **Eventos exclusivos**, quando a ocorrência de um exclui a realização do outro, igual a soma das probabilidades individuais, P(A) + P(B), ou P(A U B).

        **Eventos não exclusivo**, eventos simultâneos, igual a soma das probabilidades individuais menos a multiplicação das mesmas, P(A) + P(B) - P(A) x P(B), ou P(A U B) = (A) + P(B) - P(A interseção B).

        **Condicional**, evento A ocorre depois de evento B, número de elementos da interseção de A e B sobre número de elementos de B, P(A/B) = P(A interseção B) sobre P(B).

        **Regra da multiplicação**, ocorrência conjunta de dois eventos:

        **Ocorrência simultânea**, P(A interseção B) = P(B) x P(A / B), com ou sem reposição.
    """
)


def distribuicoes():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(paginas.keys())[5]}")
    st.write(
        """
        **Distribuição de probabilidade**, expressão matemática aplicável a múltiplas situações, respeitando determinadas premissas.

        #### Variáveis aleatórias, valores acidentais, discretas ou contínuas.

        **Variável aleatória discreta**, valores inteiros e finitos.

        **Variável aleatória contínua**, valores em um intervalo.

        **Distribuição binomial**, discreta, a cada tentativa, sempre dois resultados possíveis e exclusivos, sucesso (p) e insucesso (q), probabilidade de um evento ocorrer 'x' vezes em 'n' tentativas.

        Dados da fórmula: (N), tentativas, (X), vezes, (p), probabilidade de sucesso, (q = 1 - p), insucesso e fatoriais de N e X, este sempre igual ou menor a N.

        **Distribuição _Poisson_**, sucessos por unidade de tempo ou espaço.

        **Dados da fórmula:** (X), número de sucessos, (sinal de lambda), número médio de sucesso em intervalo específico, média e (e), base do logaritmo natural (2.71828).
    """
)


def estimacao():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(paginas.keys())[6]}")
    st.write(
        """
        **Inferência estatística**, processo para obter informações sobre uma população com base em resultados obtidos na amostra.

        **Estimativa**, valor atribuído ao estimador, grandeza baseada em observações feitas em amostra, pode ser por ponto ou intervalo.

        **Estimativa por ponto**, valor único, aproximação.

        **Estimativa por intervalo**, intervalo de confiança, faixa de valores possíveis e aceitos como verdadeiro em torno da estimativa por ponto.

        **Intervalo de confiança**, intervalo de valores com probabilidade de conter o valor desconhecido associado a um nível de confiança, um número que exprime o grau de confiança deste intervalo.

        **Fórmula:**
        C (erro amostral) igual a Z (distribuição normal padronizada) vezes delta (desvio padrão da população) sobre a raiz quadrada de n (tamanho amostral).

        O intervalo de confiança (letra grega mu, média da população) fica entre a média amostral menos o C e a média amostral mais C.

        Erro versus tamanho da amostra, inversamente proporcional, variação da fórmula de intervalo de confiança.

        Intervalo de confiança para proporções

        **Teste de hipótese**, comparar medidas, aferir correção, fazer inferências, hipótese nula (H zero), igualdade, alternativa (H um), desigualdade.

        Erros, hipótese nula ser verdeira (tipo 1) e rejeitada ou ser falsa e aceita (tipo 2).

        Regiões, rejeição e aceitação.

        **Estimador**, ...

        Fórmula, 
    """
)

def modelo():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(paginas.keys())[7]}")
    st.write(
        """
        Modelo
    """
)
    
paginas = {
    "Início": inicio,
    "Introdução": introducao,
    "Medidas de posição": medidas_posicao,
    "Medidas de dispersão": medidas_dispersao,
    "Probabilidade": probabilidade,
    "Distribuições": distribuicoes,
    "Estimação": estimacao,
    #"Modelo": modelo
}

topicos = st.sidebar.selectbox("Tópicos", paginas.keys())
paginas[topicos]()
