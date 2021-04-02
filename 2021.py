import sqlite3
import pandas as pd
from sqlalchemy import create_engine
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
cnx=create_engine('sqlite:/// bac.db').connect
from sqlite3 import dbapi2 as sqlite3
sqlippt= sqlite3.connect('weekday_db')
cursor=sqlippt.cursor()
createt_table="""create Table if not exists
'%MyTable%'(reg integer primary key unique,name text,mytime text,mydate text,weekd text);""".format(MyTable)
cursor.execute(createt_table)
print('%s created sucessfully'%(MyTable))
go=None
if int(d[1])<=11:
	go='AM'
else:
	go='PM'
ct=""" create table if not exists '{}' as select  * from '%MyTable%' """.format(MyTable)
cursor.execute(ct)
se=""" create table if not exists maintable as select * from '%MyTable%' """
cursor.execute(se)
print('maintable created sucessfully')
Trig=""" create trigger if not exists my_trig BEFORE UPDATE ON '{}'
BEGIN
     SELECT 
           CASE
               WHEN new.mytime =old.mytime
                   THEN
                             New.mytime ='{}'
                             
                              END;
   END; """.format(MyTable,h)
cursor.execute(Trig)

cft=""" create table if not exists basedata as select * from '{}' """.format(MyTable)
cursor.execute(cft)

vb=""" create trigger if not exists jmk after insert on '%MyTable%'
begin
insert into '{}' select * from '%MyTable%' ;end;""".format(MyTable)
cursor.execute(vb)
bvnn=""" create trigger if not exists flagss after update of mytime on '{}'
begin
insert into 'maintable' select * from '{}';end;""".format(MyTable,MyTable)
cursor.execute(bvnn)
gk="""create trigger if not exists bnmm after insert on '{}'
begin
update '{}' set mytime=strftime('%H:%M:%S'||'{}'  
,datetime('now','localtime')),mydate=strftime('%Y-%m-%d',datetime('now','localtime')),weekd=strftime('%w','now');end;""".format(MyTable,MyTable,go)
cursor.execute(gk)
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
			sqlippt.commit()
			print('Record inserted sucessfully')
	elif action =='S':
		while c!=None:
			d=int(input('Please enter your name for attendance:'))
			inser_me="""update '{}' set mytime=strftime('%H:%M:%S' || '{}',datetime('now','localtime')),mydate=strftime('%Y-%m-%d',datetime('now','localtime')),weekd=strftime('%w','now')where reg='{}' """.format(MyTable,go,d)
			cursor.execute(inser_me)
			sqlippt.commit()
			ko=""" update '{}' set mytime ='Absent',mydate= strftime('%Y-%m-%d',datetime('now','localtime'))where mytime is null and mydate is null """.format(MyTable)
			cursor.execute(ko)
			vm5=""" update '{}' set weekd='Friday'where weekd=5 or null""".format(MyTable)
			cursor.execute(vm5)
			vm1=""" update '{}' set weekd='Monday' where weekd=1 or null""".format(MyTable)
			cursor.execute(vm1)
			vm2=""" update '{}' set weekd='Tuesday' where weekd=2 or null""".format(MyTable)
			cursor.execute(vm2)
			vm3=""" update '{}' set weekd='Wednesday' where weekd=3 or null""".format(MyTable)
			cursor.execute(vm3)
			vm4=""" update '{}' set weekd ='Thursday' where weekd=4 or null""".format(MyTable)
			cursor.execute(vm4)
			
			fg="""select * from '{}' """.format(MyTable)
			cursor.execute(fg) 
			print(cursor.fetchall())
			for i in j:
				ty=""" insert into 'maintable' select * from '{}'  """.format(MyTable)
				cursor.execute(ty)
				op=""" select distinct * from 'maintable'   """
				cursor.execute(op)
				km=cursor.fetchall()
			dg=pd.DataFrame(km,columns=['reg','name','mytime','mydate','weekd'])
			print(dg)
			cm=""" select count(name) from 'maintable' where mytime<>'Absent' """.format(MyTable)
			cursor.execute(cm)
			#print(cursor.fetchall())
			
	
	
			
	
		  
			
			
	

 		

 		
 	
 		
 	
 
 

	

	