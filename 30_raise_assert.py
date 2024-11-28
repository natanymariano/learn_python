# Use raise para manipulação de erros explícita em produção.
# Use assert durante o desenvolvimento para verificar pressupostos ou condições que não deveriam falhar.

def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError ("n1 e n2 não podem ser negativos")
    return n1 + n2
print(soma(2, 3)) #para funcionar o raise, colocar um nº negativo aqui

print('___ASSERT_____\n')

def dividir(a, b):
    assert b != 0, "O divisor não pode ser zero."
    return a / b

print(dividir(10, 2))  # Funciona normalmente.
print(dividir(10, 0))  # Levanta AssertionError.
