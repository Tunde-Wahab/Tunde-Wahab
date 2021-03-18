from sqlite3 import dbapi2 as sqlite3

import re,time
c=time.asctime()   
a,d=(int,re.findall(r'\d+',c))
u=(c[4:7])
l=(c[0:3])
#print(l)
#print(c)
p=('%s%s%s%s%s' %(d[0],'/',u,'/',d[4]))
#print(p)
h=('%s%s%s%s%s'%(d[1],':',d[2],':',d[3]))
MyTable=d[2]
#print(h)
sqlitepooo= sqlite3.connect('pjkom_pgdb')
cursor = sqlitepooo.cursor()
createt_table="""create Table if not exists
'%MyTable%'(reg integer primary key unique,name text,mytime text,mydate text);""".format(MyTable)
cursor.execute(createt_table)
print('%s created sucessfully'%(MyTable))

ct=""" create table if not exists '{}' as select  * from '%MyTable%' """.format(MyTable)
cursor.execute(ct)
se=""" create table if not exists maintable as select * from '%MyTable%' """
cursor.execute(se)
print('maintable created sucessfully')
cft=""" create table if not exists basedata as select * from '{}' """.format(MyTable)
cursor.execute(cft)

gt=""" create trigger if not exists opppd after insert on '%MyTable%'
begin
insert into '{}' (reg,name) select reg,name from '{}'; end; """.format(MyTable,MyTable,MyTable)
cursor.execute(gt)
sqlitepooo.commit()

sdk=""" drop table 'basedata' """
cursor.execute(sdk)

g=""" select name from sqlite_master where type='table' """
cursor.execute(g)
j=cursor.fetchall()
print(j)
db={}
print('welcome to timebook project')
while True:
	print('what do you want to do')
	print('Enter R to [R]egistration,S to [S]earch,F to [F]ind record')
	print('Or enter Q to [Q] uite')
	action= input()
	if action =='R':
		while c!=None:
			x=int(input('Enter your number:'))
			y=str(input('Enter your name:')).capitalize()
			insert_table=""" insert into '%MyTable%'(reg,name) values(?,?); """.format(MyTable)
			data=(x,y)
			cursor.execute(insert_table,data)
			sqlitepooo.commit()
			print('Record inserted sucessfully')
	elif action =='S':
		while c!=None:
			d=int(input('Please enter your name for attendance:'))
			inser_me="""update '{}' set mytime=strftime('%H:%M:%S',datetime('now','localtime')),mydate=strftime('%Y-%m-%d',datetime('now','localtime')) where reg='{}' """.format(MyTable,d)
			cursor.execute(inser_me)
			sqlitepooo.commit()
			sele=""" select * from '{}' where name <> 'Admin' """.format(MyTable)
			cursor.execute(sele)
			q=cursor.fetchall()
			#print(q)
		 	
			print('success')
			ds= """ create trigger if not exists omhjdskol after update on '{}'
			when mytime is null or mytime not null
			begin
			 insert  into 'maintable'  select * from '{}';end;""".format(MyTable,MyTable)
			cursor.execute(ds)
			jk=""" select * from 'maintable' where name='Bola' """
			cursor.execute(jk)
			print(cursor.fetchall())
			
	
		  
			
			
	

 		

 		
 	
 		
 	
 
 

	

	