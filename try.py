from pymysql import *


conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
cr = conn.cursor()
q = 'select bookingId,bookId,dateOfBooking,dateOfRelease from Booking where memberId = "{}"'.format(1)
cr.execute(q)
result= cr.fetchall()
query= 'select bookName from books where bookId = "{}"'.format(20)
cr.execute(query)
result1=cr.fetchone()



for i in result:
    new1 = (i)
    new1 += result1
    print(new1)

