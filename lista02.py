from csv import list_dialects


def Erro():
    print('exercicio ainda não Criado')

def MaiorNum():
    n1=int(input('Digite um valor'))
    n2=int(input('Digite um valor'))
    if(n1>n2):
        print(n1,' maior que ',n2)
    else:
        print(n2,'maior que ',n1)

def  Sexo():
    sex=input('Qual o seu sexo\nF - Feminino, M - Masculino')
    if(sex=='F'):
        print('Feminino')
    elif(sex=='M'):
        print('Masculino')
    else:
        print('Sexo invalido para os parametros pedidos no sistema')

def Media():
    av1=int(input('Valor nota: '))
    av2=int(input('Valor nota: '))
    med=(av1+av2)/2
    if(med>=7 and med<10):
        print('Aprovado')
    elif(med==10):
        print('Aprovado com Distinção')
    else:
        print('reprovado')

def MaiorMenor():
    n1=int(input('Valor: '))
    n2=int(input('Valor: '))
    n3=int(input('Valor: '))
    if(n1>n2 and n1>n3):
        print('O maior é o ', n1)   
    elif(n2>n1 and n2>n3):
        print('O maior é o ', n2)
    else:
        print('O maior é o ',n3)
    
    if(n1<n2 and n1<n3):
        print('O menor é o ', n1)   
    elif(n2<n1 and n2<n3):
        print('O menor é o ', n2)
    else:
        print('O menor é o ',n3)

def Ordem():
        n1=int(input('Valor: '))
        n2=int(input('Valor: '))
        n3=int(input('Valor: '))
        lista=[n1,n2,n3]
        print('lista ordenada',sorted(lista))

    
    


op=int(input('Qual exercicio deseja vizualizar?\nFaça um Programa que peça dois números e imprima o maior deles. - 01\nFaça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.-03\nFaça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:\nA mensagem "Aprovado", se a média alcançada for maior ou igual a sete;\nA mensagem "Reprovado", se a média for menor do que sete;\nA mensagem "Aprovado com Distinção", se a média for igual a dez. - 05\nFaça um Programa que leia três números e mostre o maior e o menor deles - 07\nFaça um Programa que leia três números e mostre-os em ordem decrescente. - 09\n'))
    
if(op==1):
    MaiorNum()
elif(op==3):
   Sexo()
elif(op==5):
   Media()
elif(op==7):    
   MaiorMenor()
elif(op==9): 
    Ordem()
else:
    Erro()
   