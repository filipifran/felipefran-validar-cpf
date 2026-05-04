def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"

def main():
    cpf = input("Digite um CPF: ")

    if validar_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")


if __name__ == "__main__":
    main()

# Exemplo caso queira usar: 12345678909
