import pymysql

cho=None

con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
curs=con.cursor()

no=int(input("enter the prodid:"))

curs.execute("select * from MOBILES where Prodid=%d" %no)
data=curs.fetchone()

if data:
    print(data)
    cho=input("Do you want to delete?")
    if cho=='Yes'.upper():
        curs.execute("delete from MOBILES where Prodid=%d" %no)
        con.commit()
        print("mobile deleted sucessfully....")
    else:
        print("not deleted")    
else:
    print("mobile does not exist")  

con.close()          
