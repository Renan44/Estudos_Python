def formula(soma_dos_numeros):
    global soma
    digito = 11 - (soma_dos_numeros % 11)
    soma = 0
    if digito > 9:
        return '0'
    else:
        return str(digito)


def limpar_cnpj(sujo):
    global cnpj
    cnpj = [str(x) for x in sujo if x.isdigit()]
    cnpj = ''.join(cnpj)
    return cnpj


def adicionar_digito(digito):
    global cnpj_cortado
    return cnpj_cortado + digito


def obter_soma(contador):
    global soma
    for i in cnpj_cortado:
        soma += int(i) * contador
        if contador == 2:
            contador = 10
        contador -= 1


while True:
    contador, soma = 5, 0
    cnpj_cortado = limpar_cnpj(input('Insira o CPNJ: '))[:12]
    obter_soma(5)
    primeiro_digito = formula(soma)
    cnpj_cortado = adicionar_digito(primeiro_digito)
    obter_soma(6)
    segundo_digito = formula(soma)
    cnpj_cortado = adicionar_digito(segundo_digito)
    if cnpj_cortado == cnpj:
        print("Válido")
    else:
        print("Inválido")
    print(f'{cnpj}//{cnpj_cortado}')
