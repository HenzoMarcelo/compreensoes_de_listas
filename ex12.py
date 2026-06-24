palavras = ["python", "java", "Telefone"]


def extrair_letras(palavras):
    return [x for palavra in palavras for x in palavra]


print(extrair_letras(palavras))
