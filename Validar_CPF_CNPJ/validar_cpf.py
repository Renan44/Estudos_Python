cpf = input("insira o CPF: ")
cpfi = cpf[:9]


def check(x):
    if x > 9:
        y = 0
    else:
        y = x
    return y


def loop(a):
    sum = 0
    for n1 in cpfi:
        mult = int(n1) * a
        sum += mult
        a -= 1
    return sum


soma = loop(10)
calculo = 11-(soma % 11)
digito_1 = str(check(calculo))
cpfi = cpfi+digito_1
soma2 = loop(11)
calculo_2 = 11-(soma2 % 11)
digito_2 = str(check(calculo_2))
novo_cpf = cpfi+digito_2
if novo_cpf == cpf:
    print("CPF Válido")
else:
    print("CPF inválido")
print(novo_cpf)
