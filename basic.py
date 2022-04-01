import  pymysql
import pandas


con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
#curs=con.cursor()
#curs.execute("select * from MOBILES")
#data=curs.fetchall()
#print(data)

#for rec in data:
   #print(rec)

df=pandas.read_sql("select * from MOBILES",con)
print(df)
