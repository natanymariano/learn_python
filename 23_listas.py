nomes = ['Natany', 'Cleiton', 'Rosi']

nomes[0] = 'Natany Mariano' #Alterar algo na lista
nomes.append('Ilido') #Adicionar algo no final da lista. Utilizar método APPEND (acrescentar)
print(nomes [2]) #Mostar nome na posição
print(len(nomes)) #Mostrar quantidade de elementos na lista
print(nomes) #exibe a lista completa
print('=================')

#Criando uma lista com While METHOD APPEND
nomeExe = [] #comçando com a lista vazia
while True:
    nome = input('Digite -1 para sair ou cadastre um nome: ')
    if nome == '-1':
        break
    nomeExe.append(nome)
print(nomeExe)

#Inserir na lista na posição que eu quero METHOD INSERT
nomeExe2 = ['Natany', 'Milene', 'Larissa', 'Juliana']
nomeExe2.insert(0, 'Cleiton') 
print(nomeExe2)

#Remover nome da lista com METHOD POP através do INDEX (posição da String, caso a posição fique em branco, remove o último artigo da lista)
nomeExe3 = ['Natany', 'Milene', 'Larissa', 'Juliana']
nomeExe3.pop() #Remove o último nome
nomeExe3.pop(2) #Remover o nome que estiver na posição 2
print(nomeExe3)

#Remover nome da lista com METHOD REMOVE escrevendo o nome ou o valor exato
nomeExe4 = ['Natany', 'Milene', 'Larissa', 'Juliana']
nomeExe4.remove('Milene')
print(nomeExe4)

#Descobrir o index de algum elemento utilizando o METHOD INDEX
nomeExe5 = ['Carlos', 'Marcos', 'Fernanda', 'Julia']
print(nomeExe5.index('Julia'))

#Ordenar listas em ordem METHOD SORT
nomeExe6 = ['Carlos', 'Marcos', 'Fernanda', 'Julia']
nomeExe6.sort()
print(nomeExe6)