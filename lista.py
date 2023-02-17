from tokenize import Double


def receber():
    n=int(input('Diga um número: \n'))
    print('O número informado foi {}'.format(n))

def soma():
    n=int(input('Diga um número: \n'))
    n1=int(input('Diga um número: \n'))
    print('{} + {} = {}'.format(n,n1,n+n1))

def areaDobro():
    lado=int(input('Digite o valor dos lados: \n'))
    area=lado*lado
    print('o resultado da area e de {}, e o dobro disso é {}'.format(area,area*area))

def grausFToC():
    f=int(input('Quantos graus Fa Fahrenheit: \n'))
    print(f,'°F em Celsius se torna %.3f °C',5*((f-32)/9))
    
    'Questão 01'
op=int(input('Qual exercicio você deseja vizualizar\n02,03,07,09\n'))
if(op==2):
    receber()
elif(op==3):
    soma()
elif(op==7):
    areaDobro()
elif(op==9):    
    grausFToC()

