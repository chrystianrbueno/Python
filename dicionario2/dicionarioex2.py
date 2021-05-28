import copy
clientes = {
    'cliente1': {
        'nome': 'Carlos',
        'sobrenome': 'José',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Pereira',
    },
}

novo_dicionario_clientes = copy.deepcopy(clientes)

for clientes_id, clientes_value in clientes.items():
    print(f'Exibindo {clientes_id}')
    for dados_id, dados_value in clientes_value.items():
        print(f'\t{dados_id} = {dados_value}')