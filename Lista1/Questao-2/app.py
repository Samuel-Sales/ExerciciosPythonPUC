temperaturas = []
temperaturasNegativas = 0
temperaturasPositivas = 0
somaTemperatura = 0

for _ in range(5) :
    temperatura = float(input('Informe uma temperatura: '))
    temperaturas.append(temperatura)
    somaTemperatura += temperatura

    if temperatura < 0 :
        temperaturasNegativas += 1
    elif temperatura > 0 :
        temperaturasPositivas += 1

menorTemperatura = min(temperaturas)

temperatura0a20 = [temp for temp in temperaturas if 0 < temp < 20]
mediaTemperaturas = sum(temperatura0a20) / len(temperatura0a20)




print(f'A menor temperatura é {menorTemperatura}.')
print(f'A média das temperaturas entre 0 e 20 é {mediaTemperaturas:.2f}')
print(f'São {temperaturasNegativas} temperaturas negativas e {temperaturasPositivas} temperaturas positivas.')