#Tipos Primitivos str, int, float, bool

n = str(input("Digite algo: "))
print(type(n))
print(n.isnumeric())#isnumeric() verifica se a string contém apenas caracteres numéricos. Se a string contiver apenas números, o método retorna True; caso contrário, retorna False.
print(n.isalpha())#isalpha() verifica se a string contém apenas caracteres alfabéticos (letras). Se a string contiver apenas letras, o método retorna True; caso contrário, retorna False.
print(n.isalnum())#isalnum() verifica se a string contém apenas caracteres alfanuméricos (letras e números). Se a string contiver apenas letras e números, o método retorna True; caso contrário, retorna False.