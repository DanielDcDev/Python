metros = float(input('Digite uma distancia em km: '))

print('''
Em Kilometros {:.3f}.
Em hecametros {:.2f}.
Em dametros {:.1f}.
Em metros  {:.0f}.
Em decametros {:.0f}.
Em centimetros {:.0f}.
Em nanometros {:.0f}.
'''
    .format((metros/1000), (metros/100), (metros/10),metros,(metros*10),(metros*100), (metros*1000)))
