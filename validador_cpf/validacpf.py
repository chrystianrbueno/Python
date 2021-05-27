"""
Pega os 9 primeiros numeros do cpf e gera os 2 números finais
Depois compara com CPF digitado
"""
while True:
    cpf = input('Digite um cpf: ')
    #cpf = '16899535009'
    novo_cpf = cpf[:-2]

    total = 0
    reverso = 10

    for index in range(19):
        if index > 8:
            index -= 9
        print(cpf[index], index , reverso)
        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
    print('CPF válido' if (cpf == novo_cpf and not sequencia) else 'CPF inválido')
