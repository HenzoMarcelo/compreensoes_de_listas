#SEM COMPREENSAO DE LISTAS:
def achatar(lista):
    resultado = []

    for item in lista:
        if isinstance(item, list):
            resultado.extend(achatar(item))
        else:
            resultado.append(item)

    return resultado


#COM COMPREENSAO:
def achatar2(lista):
    return [
        x for item in lista
        for x in (achatar(item) if isinstance(item, list) else [item])
    ]