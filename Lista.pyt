def cadastro():
    'Nome, Endereço, Idade, Telefone, cargo, salário.'
    nome=input(('Nome:'))
    endereco=int(input('Endereco:'))
    idade=int(input('Idade:'))
    telefone=int(input('Telefone:'))
    cargo=input('Cargo:')
    salario=float(input('Salario:'))
    print("Nome: {}\nEndereço: {}\nIdade: {}\nTelefone: {}\nCargo: {}\nSalario: {}\nCadastro realizado com Sucesso!".format(nome,endereco,idade,telefone,cargo,salario))

def nomeusuario():
    'Usuário digita Nome=João e Idade=20'
    nome=input('Nome:')
    idade=int(input('Idade:'))
    anoN=2022-idade
    print('Olá {} Você nasceu em {} e tem {} anos'.format(nome, anoN, idade))

def avs():
    av1=int(input('Valor av1: '))
    av2=int(input('Valor av2: '))
    print('Valor avs'.format((av1+av2)/2))

def anosDias():
    idade=int(input('Idade: '))
    dias=idade*365
    horas=idade*8760
    segundos=idade*31557600
    print('Sua idade e:\n{}\nVoce viveu {} dias e {} horas e {} segundos'.format(dias, horas,segundos))
    

op=int(input('qual Exercicio deseja'))
if(op==1):
    cadastro()
elif(op==2):
    nomeusuario()
elif(op==3):
    avs()
elif(op==4):
    anosDias()
