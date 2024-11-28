# Código pode ser mais robusto e preparado para lidar com situações inesperadas!
n1  = int(input('Digite um número: '))
n2  = int(input('Digite um número: '))

try:
    print(n1/n2)
except:
    print('Não consegui')
finally:                    #Sempre será executado
    print('Finalizado!')

print('__________________\n')

try:
    exe2 = int(input('Digite um número: '))
    print(5/exe2)
except ValueError:
    print('Digite um número inteiro!')
except ZeroDivisionError:
    print('Não digite 0!')
