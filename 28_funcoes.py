def minha_funcao():
    print('Oi')
    print('tudo bem?')

minha_funcao()

def soma_numeros(n1, n2):
    print(n1 + n2)
soma_numeros(2, 3)

print("________________________________")

#SOBRE *ARGS: pode ser colocado outro nome ao invés do ARGS o importante é ter o "*" antes
def soma_numeros(n1, n2, *args): # *args se utiliza quando não sabemos a quantidade de parametros que uma função irá precisar 
    print(f"n1 = {n1} n2= {n2} args={args}")
soma_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)

print("________________________________")

def multiplicar(*args):
    resultado = 1
    for i in args:
        resultado *= i
    print(resultado)
   
multiplicar(2, 3, 4)

print("________________________________")

# **kwargs produz um dicionário.

def exeKwargs(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exeKwargs(nome='Natany', idade=26, pais='Portugal')        

print("________________________________")