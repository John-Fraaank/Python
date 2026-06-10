'''Tipos Primitivos'''
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
soma = n1 + n2
# A função format() é usada para formatar a string, substituindo os placeholders {n1}, {n2} e {soma} pelos valores correspondentes. O resultado é uma mensagem que exibe a soma dos dois números.
print(f"A soma de {n1} e {n2} é {soma}".format(n1, n2, soma))