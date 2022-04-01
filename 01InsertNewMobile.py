import pymysql

try:
    no=int(input("enter a number:"))
    nm=input("enter the modelname:")
    cp=input("enter the company:")
    cn=input("enter the connectivity:")
    RAM=int(input("enter the RAM:"))
    ROM=int(input("enter the ROM:"))
    cr=input("enter the color:")
    pr=input("enter the processor:")
    sc=input("enter the screen length:")
    bt=int(input("enter the battery MaH:"))
    prc=float(input("enter the price:"))
    rat=float(input("enter the rating:"))

    con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
    curs=con.cursor()

    curs.execute("insert into MOBILES values(%d,'%s','%s','%s',%d,%d,'%s','%s','%s',%d,%.2f,%.2f)" %(no,nm,cp,cn,RAM,ROM,cr,pr,sc,bt,prc,rat))
    con.commit()
    print("New Mobile data is added successfully...")
    con.close()

except Exception as e:
    print("data cannot be inserted....error in data")
