dicionario = {'chave1': 'valor da chave'}
dicionario['nova_chave'] = 'valor da nova chave'
print(str(dicionario) + '\n')


print(len(dicionario))
print(dicionario['chave1'] + '\n')

for chaves, valores in dicionario.items():
    print(chaves,valores,sep= '- ')