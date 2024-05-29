import pandas as pd
import csv 
df = pd.read_csv('./M1/Clase 04/hospitales2.csv')

df['WKT'] = df['WKT'].str.replace('POINT ', '')
df['WKT'] = df['WKT'].str.replace('(', '')
df['WKT'] = df['WKT'].str.replace(')', '')

latitude = df['WKT'].str.split(' ', expand=True)[0]
longitude = df['WKT'].str.split(' ', expand=True)[1]

datos = dict(latitude=latitude, longitude=longitude, name=df['DOM_NORMA'], label=df['NOM_MAP'])
print(datos)

pd.DataFrame(datos).to_csv('hospitales2_salida.csv', index=False)