perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}

resposta_certas = 0

for pergunta_id, pergunta_value in perguntas.items():
    print(f'{pergunta_id}: {pergunta_value["pergunta"]}')

    print('Respostas: ')
    for resposta_id, resposta_value in pergunta_value['respostas'].items():
        print(f'[{resposta_id}]: {resposta_value}')

    resposta_usuario = input("Digite a resposta ")
    if resposta_usuario == pergunta_value.get('resposta_certa'):
        print("Você acertou")
        resposta_certas += 1
    else:
        print("Você errou")
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certas/ qtd_perguntas * 100

print(f'Voce acertou {resposta_certas}')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.2f}%')