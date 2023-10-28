mesAtual = 6
somaValores = 0

for mes in range(1, 13):
    if mes < mesAtual:
        somaValores += mes
prox_mes = mesAtual + 1

par = mesAtual % 2 == 0

print("A soma dos valores menores que o mês atual é igual a {}.".format(somaValores))

print("O próximo mês é {}.".format(prox_mes))

if par:
    print("O mês atual é par.")
else:
    print("O mês atual é ímpar.")