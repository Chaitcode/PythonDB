import pymysql

con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
curs=con.cursor()

cp=input("enter the company:").lower()
curs.execute("select ModelName from MOBILES where Company='%s'" %cp)
data=curs.fetchall()

if data:
    lst=[]
    lst.append(data)
    print(lst)
else:
    print("company doesnot exist")    

con.close()    
    
 

