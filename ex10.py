lista_numerica = [1, -3, 34, 10, -9, -1, 4, 13 - 45, 0]

def numeros_positivos(lista):
    return [x for x in lista if x > 0]

print(numeros_positivos(lista_numerica))