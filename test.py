import sqlite3
import pandas as pd
print(dir(sqlite3))

conn = sqlite3.connect('crops.sql3')
crops = 'jagung.csv'
df = pd.read_csv('data/' + crops, encoding='unicode_escape', sep=';')

df.to_sql(name='crops', con=conn)

query = pd.read_sql('select * from crops limit 5', conn)

print(query)

