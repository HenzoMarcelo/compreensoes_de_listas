def numero_primo(n):
    if n < 2:
        return False
    for numero in range(2, n):
        if n % numero == 0:
            return False
    return True
    

print([x for x in range(1, int(input())) if numero_primo(x)])