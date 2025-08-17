import sqlite3

conn = sqlite3.connect('C:/Users/user/Desktop/4pychram/DB/test.db')

print('opened database sucessfully')

#conn.execute('''CREATE TABLE orders
 #               (OrderID int not null primary key,
  #              Price REAL not null,
   #             Product text not null,
    #            CustomerID INT not null,
     #           CustomerName text not null);''')

#print('table created sucessful')

#conn.execute("insert into orders(OrderID,Price,Product,CustomerID,CustomerName) values (1,10.2,'apple',101,'sam');")
#conn.execute("insert into orders(OrderID,Price,Product,CustomerID,CustomerName) values (2,20.2,'spple',201,'ram');")
#conn.execute("insert into orders(OrderID,Price,Product,CustomerID,CustomerName) values (3,30.2,'gpple',301,'jam');")
#conn.commit()
#print('records added sucesssfully')

a = conn.execute("select Price from orders;")
for i in a:
    print(i)

#conn.execute("update orders set CustomerName = 'pam' where CustomerID = 301;")
#conn.commit()
#print(str(conn.total_changes) + ': total changes no')