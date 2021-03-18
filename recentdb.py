from sqlite3 import dbapi2 as sqlite3
Reg=int(input('enter your regno:'))
Name=str(input('enter your name:'))
sqliteconn= sqlite3.connect('Sqlite_pythin')
cursor = sqliteconn.cursor()
print("connection syccessful")
create_table="""CREATE TABLE IF NOT EXISTS My_Table(Reg INTEGER PRIMARY KEY UNIQUE,Name TEXT NOT NULL);"""
cursor= sqliteconn.cursor()
cursor.execute(create_table)
Insert_param="""INSERT  OR REPLACE INTO My_Table('Reg','Name')
VALUES(?,?);"""
data_tuple=(Reg,Name)
cursor.execute(Insert_param,data_tuple)
sqliteconn.commit()	
print("student added sucessfully")
Select_Table="""SELECT Name,Reg from 'My_Table' """
cursor.execute(Select_Table)
c=cursor.fetchall()
print(c)

 