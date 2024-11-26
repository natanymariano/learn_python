#É uma estrutura de dados que pode armazenar mais de um valor, assim como as listas;
#É uma estrutura de dados que chamaos de chave e valor;
#Pode ser criado de duas maneiras: x = dict() ou x = {}
#Sempre será separado por dois pontos: x = {'nome' : 'Natany Mariano', .....}

pessoa = {'nome' : 'Natany Mariano', 'idade' : 26, 'cep' : '3750144' }
print(pessoa['nome'])

pessoa['nome'] = 'Cleiton' #Para alterar algum valor da chave
print(pessoa) #Iá mostrar a chave completa, porém com o nome alterado

print('_______________________')

exe2 = {'nomes' : [], 'idade' : 21} #Criando uma lista na posição NOMES
exe2['nomes'].append('Natany Mariano')
exe2['nomes'].append('Cleiton Minas')
print(type(exe2['nomes'])) #para visualizar que o tipo de dados que é a chave NOME, nesse caso é uma list (lista)
print(type(exe2['idade']))
print(exe2)
print(exe2['nomes'][1]) #para visualizar o conteúdo da chave NOME e a posição exata

print('_______________________')

exe3 = [{'nome' :'Natany Mariano', 'idade' : 26, 'país' : 'Portuagal'},
        {'nome' : 'Cleiton Minas', 'idade' : 43, 'país' : 'Portugal'},
        {'nome' : 'Rosimar Ribeiro', 'idade' : 57, 'país' : 'Brasil'} ]

print(type(exe3)) 

for pessoaExe3 in exe3:
    print(pessoaExe3)
    print(type(pessoaExe3))