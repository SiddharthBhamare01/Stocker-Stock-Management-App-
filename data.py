from sqlite3 import *

con = connect('stocker.db')
cursor = con.cursor()
#sql = "drop table stockinfo"
sql = "create table stockinfo (company_name text,investment_price float,quantity int)"
cursor.execute(sql)
#for d in data:
#    print(d[0])
#    print(d[1])
#cursor.execute(sql)
con.commit()
print("Table Created")