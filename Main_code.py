# Obtendo o valor total
Renda_mensal = float(input('Coloque com sua renda mensal:'))

# obtendo as porcentagens
obter_50_porcento = (50 / 100) * Renda_mensal
obter_30_porcento = (30 / 100) * Renda_mensal
obter_20_porcento = (20 / 100) * Renda_mensal

print("==========\nSeus números de 50% 30% 20%\n==========")

print('Necessidades:R${:,.2f}'.format(obter_50_porcento))
print('Gastos:R${:,.2f}'.format(obter_30_porcento))
print('Poupança:R${:,.2f}'.format(obter_20_porcento))

print("\n=================================================")