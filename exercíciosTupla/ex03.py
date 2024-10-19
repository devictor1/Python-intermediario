# Dada uma tupla de números inteiros, crie uma função que receba essa tupla como argumento e retorne uma nova tupla apenas com os números pares.

tuplaNumeros = (1,2,3,4,5,6,7,8,9,0)

def par():
    novaTupla = ()
    for i in tuplaNumeros:
        if i % 2 == 0 and i != 0:
            novaTupla += (i,)
    return print(novaTupla)
par()