#!/usr/bin/env python3
import pandas as pd
import pyodbc

data=pd.read_csv('/Users/user/Desktop/products.csv')
df=pd.DataFrame(data)
print(df)

server = '85.174.236.59,1435' 
database = 'test' 
username = 'sa' 
password = 'T12345678+'  
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor=conn.cursor()

for row in df.itertuples():
    cursor.execute('''
                delete from py 
                ''',

                  )

for row in df.itertuples():
    cursor.execute('''
                insert into py (col1, col2, col3)
                values (?,?,?)
                ''',
               
                row.col1,
                row.col2,
                row.col3
                  )
conn.commit()
