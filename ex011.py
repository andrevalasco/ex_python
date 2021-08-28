l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = l * h
tinta = a / 2
print('Sua parede tem dimensão {}X{} e sua área é de {} m²'.format(l, h, a))
print('Será necessário {:.2f} l de tinta para pintar esta parede'.format(tinta))