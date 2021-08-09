from pymysql import *


conn = Connect(host='127.0.0.1', user='root', password='', database='library_management')
cr = conn.cursor()

q1 = 'select booksalloted from addmembership where mID= "{}"'.format(1)
cr.execute(q1)
result = cr.fetchone()
for i in result:
    new = i-1

print(new)