notas_alunos = [1.0, 5.5, 5.1, 10, 4.9, 7, 8]


def acimadamedia(notas):
    return [x for x in notas if x > 5]


print(acimadamedia(notas_alunos))
