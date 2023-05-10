arquivo = open("dados.txt", "r")

conteudo = arquivo.readline() 
nextContent = arquivo.readline()
print('Tipo do conteúdo: ', type(conteudo))

print('Conteudo retornado pelo readLine: ')
print(repr(conteudo))



print("Próximo Conteúdo retornado: ", repr(nextContent))
print()

arquivo.close()