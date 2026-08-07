def is_prime(number):
    if number > 1:
        limite = number ** 0.5
        for i in primos:
            if i <= limite:
                if number % i == 0:
                    return False
        return True
    else:
        return False


primos = [2, 3, 5, 7, 11, 13, 17, 19]

while True:
    number = int(input("insira um numero (max 20) e -1 para sair: "))
    
    if number == -1:
        break
    
    if is_prime(number):
        print("\n", number, "é primo")
    else:
        print("\n", number, "não é primo")

print("\nPrograma encerrado.")