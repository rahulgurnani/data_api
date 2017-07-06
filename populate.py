import sqlite3
import pandas as pd

data = pd.read_csv('Mobile_Food_Facility_Permit.csv')

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
result = c.execute('SELECT * FROM api_app_foodpermit')
rows = result.fetchall()
for row in rows:
	print row

conn.close()