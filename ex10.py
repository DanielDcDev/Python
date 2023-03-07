largura = float(input('Largura da parede: '))
altura = float(input('Altura de parede: '))

print('Sua parede tem a dimensão de {:.1f} x {:.1f} e a sua área é de {:.1f}m².'.format(largura, altura, largura*altura))
print('Para pintar a parede, você precisará de {:.1f} de tinta.'.format((largura*altura)/2))