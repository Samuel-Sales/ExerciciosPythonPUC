numeroMeses = int(input("Informe o número de meses desejado: "))
quilosDesejados = float(input("Informe a quantidade de quilos que deseja perder: "))

quilosPorMes = quilosDesejados / numeroMeses

for mes in range(1, numeroMeses + 1):
    print(f"Mês {mes} você irá perder {quilosPorMes:.2f} KG")

print(f"Número de meses {numeroMeses} com uma meta de {quilosDesejados:.2f} KG.")
