# projeto bussola

import random

def bussola():
    direcao = random.randint(0,7)
    pontosCardeais = ["Norte", "Nordeste", "Leste", "Sudeste", "Sul", "Sudoeste", "Oeste", "Noroeste"]

    print("Você está indo em direção ao",pontosCardeais[direcao])

bussola()