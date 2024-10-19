# Crie duas tuplas: uma com números pares e outra com números ímpares. Concatene essas tuplas e depois repita a nova tupla 3 vezes.

pares = (2,4,6,8,10)
impares = (1,3,5,7,9)
numeros = pares + impares

for i in range(3):
    numeros += numeros
print(numeros)