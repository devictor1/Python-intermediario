# Dada a tupla cores = ('vermelho', 'azul', 'verde', 'azul', 'amarelo', 'azul'), escreva um código que conte quantas vezes a cor "azul" aparece na tupla.

cores = ('vermelho', 'azul', 'verde', 'azul', 'amarelo', 'azul')
contador = 0
for cor in cores:
    if cor == "azul":
        contador += 1
print("A coz azul aparece",contador,"vezes")