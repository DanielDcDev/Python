real= float(input('Quanto dinheiro você tem na carteira: '))

print('''
USD {:.2f}.
CAD {:.2f}.
EUR {:.2f}.
CHF {:.2f}.
'''
      .format(real/5.19,real/3.77, real/5.48, real/5.51))