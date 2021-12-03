import psycopg2
import matplotlib.pyplot as plt

conn=psycopg2.connect(database='db',user='postgres',password='pw',host='10.120.10.11',port='5432')
cursor=conn.cursor()

cursor.execute("select gmsfhm,picture from gg_gaj_rk_picture limit 10")

data=cursor.fetchall()
conn.commit()

