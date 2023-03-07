varOriginal= float (input('Qual o preço do produto? R$ '))
desconto = float(input('Qual o valor do desconto: '))
novo= varOriginal-(varOriginal*desconto/100)
print('''
O produto que custava R$ {:.2f}.
Sofrendo um desconto de {:.1f}%
O valor final ficou R$ {:.2f}.
O valor modificado foi de {:.2f}.
'''.format(varOriginal, desconto,novo,((desconto*100)/varOriginal)))