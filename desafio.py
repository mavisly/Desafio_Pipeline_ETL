import csv
"""
Extração (extract):
  - Ler o arquivo csv
  - Organizar os dados numa lista
"""

arquivo = open('lista.csv')
info = csv.reader(arquivo)

"""
  Transformação (transform):
  - Verificar quantas revisões já foram feitas
  - O padrão de revisões por ciclo é de 4 (quatro), ou seja:
   1 revisão: faltam 3
   2 revisões: faltam 2
   3 revisões: faltam 1
   4 revisões: não há mais necessidade de revisão

   - Criar um novo item na lista para guardar os novos dados
"""
tabela = list()
for revisao in info:
    if revisao[1] == 1:
        revisao.append("Faltam 3 revisões para terminar o ciclo!")
        tabela.append(revisao)

    elif revisao[1] == 2:
        revisao.append("Faltam 2 revisões para terminar o ciclo!")
        tabela.append(revisao)

    elif revisao[1] == 3:
        revisao.append("Falta 1 revisão para terminar o ciclo!")
        tabela.append(revisao)

    elif revisao[1] == 4:
        revisao.append("Você terminou seu ciclo de revisões!")
        tabela.append(revisao)
    else:
       print("Número inválido")
    