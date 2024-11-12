# and, or, not

operador = True and False #(AND: basta ter 1 FALSE que ele ja devolve FALSE)
operador2 = False or True #(OR: basta ter 1 verdadeiro que ele ja devolve VERDADEIRO)
operador3 = not False

teste1 = 5 == 5 and 12 > 20 #a partir do momento que uma operação é falsa, todo o teste1 é considerado falso
teste2= 5 == 5 and 12 < 20 #quando tudo é verdadeiro, o teste2 devolve verdadeiro


print(teste2)