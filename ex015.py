dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
totalDias = dias * 60
totalKm = km * 0.15
print('O total a pagar é de R${:.2f}'.format(totalDias + totalKm))