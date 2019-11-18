import pandas as pd

dados = pd.read_excel("/home/tom/Documentos/python/EstEProb/src/TurmaPM_Grupo_4.xlsx")

pd.options.display.html.table_schema = True
pd.options.display.max_rows = None

dados
