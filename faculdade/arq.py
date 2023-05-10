arquivo = open('dados.txt', 'r')

estudo = arquivo.readline() 
print('Tipo do conteúdo: ', type(estudo))

print('Conteudo retornado pelo read: ')
print(repr(estudo))

arquivo.close()