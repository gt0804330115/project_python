import cx_Oracle as cx

con = cx.connect('taeca/mis5@192.168.169.69:1521/ORCL')
cursor = con.cursor()
cursor.execute("select * from Sys_SelfDef_BizDic where DicNodeValue=72")
data = cursor.fetchone()
print(data)
con.close()
