# 🌞 Modelagem Matemática da Geração de Energia Solar — Sprint 1 (GoodWe)

Este projeto tem como objetivo aplicar conceitos de modelagem matemática para representar a geração de energia solar ao longo do dia, utilizando dados reais extraídos da plataforma PVWatts.

📊 O que foi feito:
Coleta de dados horários (6h às 18h) da geração de energia solar (em kW) de um sistema fotovoltaico de 4kW.
Ajuste de uma função polinomial de 2º grau para modelar a curva de geração ao longo do tempo.
Visualização da curva com gráficos em Python e Scilab.
Geração de uma tabela formatada para documentação.
Conclusão baseada na análise gráfica do comportamento da curva solar.

📈 Equação obtida:
E(t) = -30.2551t^2 + 687.4344t - 2649.5879
Essa função estima a geração de energia solar (em kW) em função do horário t (de 6h a 18h), com base nos dados do dia analisado.
