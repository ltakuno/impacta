from funcoes import celsiu2Fahrenheit

celsius = float(input('Digite o valor em graus Celsius:'))
fahr = celsiu2Fahrenheit(celsius)
print("%.2f graus celsius é igual %.2f fahrenheit " % (celsius, fahr))
