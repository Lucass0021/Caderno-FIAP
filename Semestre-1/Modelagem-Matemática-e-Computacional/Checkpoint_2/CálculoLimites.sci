// Nome: Lucas Alves Antunes Almeida
// RM: 566362

// ======================
// EXERCÍCIO 1
// ======================
x1 = [0.9, 0.99, 0.999, 1.001, 1.01, 1.1];
f1 = x1 + 1; // Função simplificada: x + 1

disp("Exercício 1: lim(x->1) (x^2 - 1)/(x - 1) = x + 1");
disp([x1', f1'], "x | f(x)");


// ======================
// EXERCÍCIO 2
// ======================
x2 = [1.9, 1.99, 1.999, 2.001, 2.01, 2.1];
f2 = x2 - 2; // Função simplificada: x - 2

disp("Exercício 2: lim(x->2) (x^2 - 4x + 4)/(x - 2) = x - 2");
disp([x2', f2'], "x | f(x)");
