import pymysql

con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
curs=con.cursor()

nm=input("enter modelname:")
pr=input("enter pupose:")

curs.execute("update MOBILES set Purpose='%s' where ModelName='%s'" %(pr,nm))
con.commit()
print("updated successfully....")
con.close()