def Cadastro():
    'Nome, Endereço, Idade, Telefone, cargo, salário.'
    nome=input(('Nome:'))
    endereco=int(input('Endereco:'))
    idade=int(input('Idade:'))
    telefone=int(input('Telefone:'))
    cargo=input('Cargo:')
    salario=float(input('Salario:'))
    print("Nome: {}\nEndereço: {}\nIdade: {}\nTelefone: {}\nCargo: {}\nSalario: {}\nCadastro realizado com Sucesso!".format(nome,endereco,idade,telefone,cargo,salario))

def Nomeusuario():
    'Usuário digita Nome=João e Idade=20'
    nome=input('Nome:')
    idade=int(input('Idade:'))
    anoN=2022-idade
    print('Olá {} Você nasceu em {} e tem {} anos'.format(nome, anoN, idade))

def Avs():
    av1=int(input('Valor av1: '))
    av2=int(input('Valor av2: '))
    print('Valor avs'.format((av1+av2)/2))

def AnosDias():
    idade=int(input('Idade: '))
    dias=idade*365
    horas=idade*8760
    segundos=idade*31557600
    print('Sua idade e:\n{}\nVoce viveu {} dias e {} horas e {} segundos'.format(dias, horas,segundos))
    
def MaiorNumero():
    
    for i in (0,5):
        numeros=int(input('numeros: '))
        if( maior<numeros):
             maior=numeros
    print('O maior numero:'.format(maior))

def TipoHumanos():
    idade=int(input('Qual sua idade:'))
    if(idade>=5)and(idade<=7):
        print('Você é um infantil A')
    elif(idade>=8)and(idade<=10):
        print('Você é um infantil B')
    elif(idade>=11)and(idade<=13):
        print('Você é um juvenil A')
    elif(idade>=14)and(idade<=17):
        print('Você é um juvenil B')
    elif(idade<=18):
        print('Você é um adulto')
    else:
        print('Impossivel Definir tente novamente')

def InteiroNegativo():
    num=int(input('Digite um número: '))
    if(num)

op=int(input('qual Exercicio deseja'))
if(op==1):
    Cadastro()
elif(op==2):
    Nomeusuario()
elif(op==3):
    Avs()
elif(op==4):
    AnosDias()
elif(op==5):
    MaiorNumero()
elif(op==6):
    TipoHumanos()
elif(op==7):
    InteiroNegativo()