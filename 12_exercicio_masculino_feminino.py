# Receba F para feminino e M para masculino e exiba o sexo da pessoa

pergunta = str(input("Qual seu sexo F ou M? "))

if pergunta == "F" or pergunta == "f":
    print("Sexo femino")
elif pergunta == "M" or pergunta == "m":
    print("Sexo masculino")
else:
    print("Tente outra vez só com F ou M ")