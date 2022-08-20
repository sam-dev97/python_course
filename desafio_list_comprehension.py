"""
    Exercício proposto:
    — Criar uma função que recebe uma string 0123456789 seis vezes sem separadores, separe essa string
em dez strings dentro de uma lista e depois transforme novamente em uma string única separada por pontos.
    Exemplo:
    Entrada:        01234567890123456789
    Primeiro passo: ["0123456789","0123456789",]
    Saída final:    0123456789.0123456789
"""

string = '012345678901234567890123456789012345678901234567890123456789'
step = 10


def separador(x):
    dez_em_dez = [
        x[indice:indice + step]
        for indice in range(0, len(x), step)
    ]

    dez_em_dez = '.'.join(dez_em_dez)
    return dez_em_dez


string_trabalhada = separador(string)

print(string_trabalhada)
