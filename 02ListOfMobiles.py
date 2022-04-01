import pymysql

con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
curs=con.cursor()
curs.execute("select ModelName from MOBILES order by Price")
data=curs.fetchall()
#print(data)

lst=[]
lst.append(data)
print(lst)    

con.close()