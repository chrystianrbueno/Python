variavel = ['Chrystian Rocha','Juca','Maria']

comeca_com_j = False

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digitar apenas uma letra por vez')
    else:
        break

for valor in variavel:
    if valor.lower().startswith(letra):
        print(valor)
