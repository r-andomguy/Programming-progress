import requests

link = 'https://TESTE1.backupdti.repl.com'

requisition = requests.get(link)

print(requisition)
print(requisition.json)

dictionary = requisition.json()

print(dictionary['sales_amount'])
