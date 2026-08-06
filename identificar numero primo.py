def is_prime(number):
    if number > 1:
        limite = number ** 0.5        # guarda a raiz numa variável separada
        for i in range(len(primos)):
            if primos[i] < limite:
                if number % primos[i] == 0:   # usa o number ORIGINAL
                    return False
            # não faz mais nada aqui — não retorna True ainda
        return True                    # só depois de testar todos, sem achar divisor
    else:
        return False

primos=[2,3,5,7,11,13,17,19]

for i in range(1, 20):
 if is_prime(i + 1):
    print(i + 1, end=" ")
print()