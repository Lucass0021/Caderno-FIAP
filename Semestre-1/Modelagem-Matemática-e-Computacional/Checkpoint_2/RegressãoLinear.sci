// Dados
Temp = [27.5,28,28.2,27.8,26.5,25.5,25,25.3,26,27,27.5,28.1];
Consumo = [45000,47000,48500,46000,42000,40000,39500,41000,42500,44000,45500,48000];
CargaT = [52,55,58,50,43,40,38,42,44,48,50,56];

// ===== Gráfico 1: Temperatura =====
[AT, BT] = reglin(Temp, Consumo);
x1 = linspace(min(Temp), max(Temp), 100);
y1 = AT * x1 + BT;
eq1 = msprintf("y = %.2f·x + %.2f", AT, BT);

scf(1);
plot(Temp, Consumo, 'ro');          // pontos
plot(x1, y1, 'b-');                 // reta
xtitle("Consumo vs Temperatura Média", "Temperatura (°C)", "Consumo (kWh)");
legend("Dados", eq1, "location", "best");
xgrid();

// ===== Gráfico 2: Carga de Trabalho =====
[AP, BP] = reglin(CargaT, Consumo);
x2 = linspace(min(CargaT), max(CargaT), 100);
y2 = AP * x2 + BP;
eq2 = msprintf("y = %.2f·x + %.2f", AP, BP);

scf(2);
plot(CargaT, Consumo, 'go');        // pontos
plot(x2, y2, 'm-');                 // reta
xtitle("Consumo vs Carga de Trabalho", "Carga (milhares horas GPU)", "Consumo (kWh)");
legend("Dados", eq2, "location", "best");
xgrid();

