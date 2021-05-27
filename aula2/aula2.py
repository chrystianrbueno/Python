secreto = 'teste'

digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print ('Digitar apenas uma letra por vez')
        continue

    # add ao final da lista de letras encontradas
    digitadas.append(letra)

    if letra in secreto:
        print(f'a letra {letra} existe na palavra secreta')
    else:
        print(f'a letra {letra} não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario  = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
       print(f'Voce acertou e a palavra era {secreto_temporario}')
       break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'Voce ainda tem: {chances} chances \n')
