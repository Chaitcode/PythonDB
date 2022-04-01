import pymysql


con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
curs=con.cursor()

no=int(input("enter the prodid:"))

curs.execute("select * from MOBILES where Prodid=%d" %no)
data=curs.fetchone()

if data:
    prc=float(input("enter the new price:"))
    curs.execute("update MOBILES set Price=%.2f where Prodid=%d" %(prc,no))
    con.commit()
    print("price of the mobile updated")
else:
    print("mobile does not found")

