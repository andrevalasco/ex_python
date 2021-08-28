salario = float(input('Digite o salário do funcionário: '))
aumento = salario +(salario * 0.15)
print('O funcionário recebia R${} e com um aumento de 15% passará a receber R${:.2f}'.format(salario, aumento))