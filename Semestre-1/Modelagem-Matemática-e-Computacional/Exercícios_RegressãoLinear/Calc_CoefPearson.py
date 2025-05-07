'''
Nome: Lucas Alves Antunes Almeida
RM: 566362
'''

'''
Situação-Problema: A cidade hipotética de Solária, localizada em uma região tropical,
está realizando um estudo sobre o consumo de energia elétrica da população ao longo 
dos meses do ano, visando compreender os fatores que mais impactam na demanda 
energética residencial. Foram coletados dados de três variáveis ao longo de 12 meses.

a) Consumo de energia elétrica residencial médio mensal (kWh); (b) Temperatura média mensal (°C)
e (c) Precipitação média mensal (mm). Com base nos dados faça o que é sugerido:

'''
from scipy.stats import pearsonr

# Dados
temperatura = [32, 31, 29, 27, 24, 20, 18, 22, 26, 28, 30, 33]
precipitacao = [130, 85, 190, 40, 75, 110, 60, 125, 95, 160, 50, 140]
consumo = [410, 400, 380, 360, 340, 310, 300, 320, 355, 370, 390, 420]


# Função para analisar correlação e imprimir resultados formatados
def analisar_correlacao(x, y, nome_variavel):
    r, p_valor = pearsonr(x, y)
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
analisar_correlacao(temperatura, consumo, "Temperatura Média (°C)")
analisar_correlacao(precipitacao, consumo, "Precipitação Média (mm)")
