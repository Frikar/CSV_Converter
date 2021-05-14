import pandas as pd
from datetime import date

#Leer el archivo CSV
df = pd.read_csv('data.csv', sep="|")

#Configurar fecha del día
date = date.today()
format_date = str(date.day) + '-' + str(date.month) + '-' + str(date.year)

#Crear el archivo de Excel con la información
data = pd.ExcelWriter('Convertidos/data.' + format_date + '.xlsx')
df.to_excel(data, index=False)
data.save()
