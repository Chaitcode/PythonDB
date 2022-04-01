import pymysql

lst=[]

ram=int(input("enter the ram :"))
rom=int(input("enter the rom :"))

con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
curs=con.cursor()
curs.execute("select ModelName from MOBILES where RAM=%d and ROM=%d" %(ram,rom))
data=curs.fetchall()

if data:
    lst.append(data)
    print(lst)
else:
    print("ram-rom storage space combination not found")


con.close()
