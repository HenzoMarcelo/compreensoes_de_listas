def descendentes(arvore):
    if arvore[1] == []:
        return []
    
    return [nome for nome, _ in arvore[1]] +\
           [nome for f in arvore[1] for nome in descendentes(f)]