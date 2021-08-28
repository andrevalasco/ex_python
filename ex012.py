prod = float(input('Qual é o preço do produto? '))
desc = prod - (prod * 0.05)
print ('O produto que custava R${}, na promoção com desconto de 5% irá custar R${:.2f}'.format(prod, desc))