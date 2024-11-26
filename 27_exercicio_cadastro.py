#Faça um programa que o usuário possa cadastrar n pessoas,
#armazenando seu nome, idade e altura

pessoas = []
while True: #quando eu não sei quantos valores o usuário quer, eu utilizo o WHILE: True
    decisao = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair ' ))
    if decisao == 2:
        break
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    pais = input('Digite o país: ')
    dict_pessoa = {'nome' : nome, 'idade' : idade, 'país' : pais}    #criar um dicionário para receber todos os dados das pessoas
    pessoas.append(dict_pessoa) #pegar todos os dados do dicionário, e adicionar na lista pessoas
print(pessoas)

for pessoa in pessoas:
    print(pessoa)