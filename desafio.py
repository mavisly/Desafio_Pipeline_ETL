import csv
"""
Extração (extract):
  - Ler o arquivo csv
  - Organizar os dados numa lista
"""

arquivo = open('lista.csv')
info = csv.reader(arquivo)

