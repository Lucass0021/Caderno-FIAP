// Nome: Lucas Alves Antunes Almeida
// RM: 566362

// Dados
temperatura = [32 31 29 27 24 20 18 22 26 28 30 33];
precipitacao = [130 85 190 40 75 110 60 125 95 160 50 140];
consumo = [410 400 380 360 340 310 300 320 355 370 390 420];

// ===== Gráfico 1: Temperatura =====
[AT, BT] = reglin(temperatura, consumo);  // Regressão linear

x1 = linspace(18, 33, 100);               // Pontos para reta
y1 = AT * x1 + BT;

// Monta string da equação formatada
eq1 = msprintf("y = %.2f·x + %.2f", AT, BT);

// Gráfico 1
scf(1);
plot(temperatura, consumo, 'ro');         // pontos
plot(x1, y1, 'b-');                        // reta
xtitle("Consumo vs Temperatura Média", "Temperatura (°C)", "Consumo (kWh)");
legend("Dados", eq1, "location", "best");
xgrid();

// ===== Gráfico 2: Precipitação =====
[AP, BP] = reglin(precipitacao, consumo); // Regressão linear

x2 = linspace(40, 190, 100);
y2 = AP * x2 + BP;

eq2 = msprintf("y = %.2f·x + %.2f", AP, BP);

// Gráfico 2
scf(2);
plot(precipitacao, consumo, 'go');
plot(x2, y2, 'm-');
xtitle("Consumo vs Precipitação Média", "Precipitação (mm)", "Consumo (kWh)");
legend("Dados", eq2, "location", "best");
xgrid();
