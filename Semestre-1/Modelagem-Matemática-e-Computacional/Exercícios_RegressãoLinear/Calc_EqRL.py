'''
Nome: Lucas Alves Antunes Almeida
RM: 566362
'''
from scipy.stats import linregress

# Dados
temperatura = [32, 31, 29, 27, 24, 20, 18, 22, 26, 28, 30, 33]
precipitacao = [130, 85, 190, 40, 75, 110, 60, 125, 95, 160, 50, 140]
consumo = [410, 400, 380, 360, 340, 310, 300, 320, 355, 370, 390, 420]

# Função para calcular e exibir regressão linear
def regressao_linear(x, y, nome_variavel):
    resultado = linregress(x, y)
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
regressao_linear(temperatura, consumo, "Temperatura Média (°C)")

# Regressão para Precipitação
regressao_linear(precipitacao, consumo, "Precipitação Média (mm)")
