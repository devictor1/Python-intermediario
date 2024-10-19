# 5) Conte quantas vezes o número 2 aparece na tupla (1, 2, 2, 3, 4, 2).

tuplaNumeros = (1,2,2,3,4,2)
contadora = 0
for i in tuplaNumeros:
    if i == 2:
        contadora+=1
print("O número 2 aparece",contadora,"vezes")