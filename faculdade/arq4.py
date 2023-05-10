def split():
    frase1 = "Eu amo comer amoras no café da manhã"
    lista_termos1 = frase1.split()
    print(lista_termos1)

    frase2 = "amora abacaxi abacate banana"
    lista_termos2 = frase2.split()
    print(lista_termos2)

    frase3 = "Carro, moto,avião"
    lista_termos3 = frase3.split(',')
    print(lista_termos3)

def split2():
    frase = "Eu amo comer amoras no café da manhã"
    #resultado obtido utilizando só o count
    print("Contagem Direta: ", frase.count('amo'))
    #resultado obtido utilizando a quebra da frase em palavras
    contador = 0
    lista_termos = frase.split()
    for termo in lista_termos:
        if termo == 'amo':
            contador += 1
    print("Contagem correta: ", contador)

def join():
    minha_lista = ['Arroz', 'Feijao', 'Macarrao']
    texto1 = ', '.join(minha_lista)
    with open('texto1.txt', 'w') as arquivo:
        arquivo.write(texto1)
    texto2 = '\n'.join(minha_lista)
    with open('texto2.txt', 'w') as arquivo:
        arquivo.write(texto2)
    print('Documentos Criados com sucesso')

arq = int(input("Qual exercicio você deseja ver: "))
if arq == 1:
    split()
elif arq == 2:
    split2()
elif arq == 3:
    join()