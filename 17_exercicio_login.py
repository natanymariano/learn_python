#Defina um usuário e senha e depois verifique se login do usuário é válido.

usuario = 'natany'
senha = 'natany12'

while True:
    usuario_login = input('Digite seu uuário: ')
    senha_login = input('Digite sua senha: ')

    if usuario_login == usuario and senha_login == senha:
        print('Você foi logado no sistema')
        break
    else: 
        print('Usário ou senha inválido')