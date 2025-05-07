'''
Nome: Lucas Alves Antunes Almeida
RM: 566362
'''

'''
Questão 1 - Um grande provedor de serviços em nuvem está monitorando o consumo de energia elétrica de seus data centers voltados à execução de cargas de trabalho com Inteligência Artificial (IA). Ao longo de 12 meses, foram coletadas informações de três variáveis:

- Consumo de energia elétrica (kWh) por mês de um cluster de IA. 
- Temperatura interna média (°C) por mês do data center no mesmo período. 
- Carga de trabalho por mês de uso de IA (milhares de horas de GPU). 

'''

# a) Análise de Correlação

from scipy.stats import pearsonr

# Dados
Temp = [27.5,28,28.2,27.8,26.5,25.5,25,25.3,26,27,27.5,28.1]
Consumo = [45000,47000,48500,46000,42000,40000,39500,41000,42500,44000,45500,48000]
CargaT = [52,55,58,50,43,40,38,42,44,48,50,56]

# Função para analisar correlação e imprimir resultados formatados
def analisar_correlacao(x,y, nome_variavel):
    r, p_valor = pearsonr(x,y)
    print(f"\n📊 Correlação entre Consumo de Energia e {nome_variavel}:")
    print(f"   ➤ Coeficiente de Pearson: {r:.3f}")
    print(f"   ➤ Valor-p: {p_valor:.2e}")

    # Interpretação da força
    if abs(r) < 0.3:
        forca = "fraca"
    elif abs(r) < 0.7:
        forca = "moderada"
    else:
        forca = "forte"

        # Significância estatística
    significancia = "significativa" if p_valor < 0.05 else "não significativa"

    print(f"   ➤ Interpretação: Correlação {forca} e {significancia}.")

# Chamadas da função para os dois casos
analisar_correlacao(Temp, Consumo, "Temperatura Média (°C)")
analisar_correlacao(CargaT, Consumo, "Carga de Trabalho média (milhar de hora de GPU)")

# b) Modelagem

from scipy.stats import linregress

# Dados já listados anteriormente (Temp, Consumo e CargaT)

# Função para calcular e exibir regressão linear
def regressao_linear(x,y, nome_variavel):
    resultado = linregress(x,y)
    a = resultado.slope
    b = resultado.intercept
    erro_a = resultado.stderr
    erro_b = resultado.intercept_stderr
    r = resultado.rvalue
    p = resultado.pvalue

    print(f"\n📈 Regressão Linear: Consumo = A * {nome_variavel} + B")
    print(f"   ➤ A (inclinação): {a:.2f} ± {erro_a:.2f}")
    print(f"   ➤ B (intercepto): {b:.2f} ± {erro_b:.2f}")
    print(f"   ➤ Coeficiente de correlação (r): {r:.3f}")
    print(f"   ➤ Valor-p: {p:.2e}")

# Regressão para Temperatura
regressao_linear(Temp, Consumo, "Temperatura Média (°C)")

# Regressão para Carga de Trabalho
regressao_linear(CargaT, Consumo, "Carga de Trabalho média (milhar de hora de GPU)")
