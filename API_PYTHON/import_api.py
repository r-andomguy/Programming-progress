import requests

link = 'https://TESTE1.backupdti.repl.com'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json)

dicionario = requisicao.json()

print(dicionario['total_vendas'])