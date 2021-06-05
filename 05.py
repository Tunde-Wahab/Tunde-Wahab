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
MyTable=p
#print(h)
go=None
if int(d[1])<=11:
	go='AM'
else:
	go='PM'
from sqlite3 import dbapi2 as sqlite3
sqlidddp= sqlite3.connect('bpkmkhyo_db')
cursor=sqlidddp.cursor()
a=""" create table if not exists tud(reg integer primary key ,name text,mytime text,mydate text,weekday text);"""
cursor.execute(a)
b=""" create table if not exists maintable(reg integer,name text,mytime text,mydate text,weekday text);"""
cursor.execute(b)
c=""" create table if not exists '{}'(reg integer,name text,mytime text,mydate text,weekday text);""".format(MyTable)
cursor.execute(c)
d=""" create trigger if not exists bbkoqm after insert on tud

begin
insert into maintable(reg,name,mytime,mydate,weekday)select reg,name, 'Absent',strftime('%Y/%m/%d',datetime('now','localtime')),weekday from tud ;end;"""
cursor.execute(d)
fc=""" create trigger if not exists hhummpy after insert on maintable
when new.name='Bac'
begin
delete from maintable where name ='Bac' ;end;"""
cursor.execute(fc)
g=""" select name from sqlite_master where type='table' """
cursor.execute(g)
j=cursor.fetchall()
print(j)

db={}
print('welcome to timebook project')
while True:
	print('what do you want to do')
	print('Enter R to [R]egistration,S to [S]earch,F to [F]ind record')
	print('enter D to [D]aily attendance')
	print('Enter I to [I]ndividual daily attendance:')
	action= input()
	if action == 'R':
		while c!=None:
			#x=int(input('Enter your number:'))
			y=str(input('Enter your name:')).capitalize()
			insert_table=""" insert into tud(name) values('{}'); """.format(y)
			
			cursor.execute(insert_table)
			sqlidddp.commit()
			print('Record inserted sucessfully')
			ft=""" select last_insert_rowid()"""
			cursor.execute(ft)
			fz=cursor.fetchone()
			fr=""" select name from maintable where reg =last_insert_rowid()"""
			cursor.execute(fr)
			ky=cursor.fetchone()
			print('%s Your registration number is %s'%(ky,fz))
	elif action == 'S':
		while c!=None:
			d=int(input('Please enter your name for attendance:'))
			inser_me="""update 'maintable' set mytime=strftime('%H:%M:%S' || '{}',datetime('now','localtime')),mydate=strftime('%Y/%m/%d',datetime('now','localtime')),weekday= strftime('%w','now')where reg='{}' 
			 """.format(go,d)
			cursor.execute(inser_me)
			sqlidddp.commit()
			d0=""" update 'maintable' set weekday ='Sunday' where  weekday =0"""
			cursor.execute(d0)
			d1=""" update 'maintable' set weekday='Monday' where weekday=1"""
			cursor.execute(d1)
			d2=""" update 'maintable' set weekday='Tuesday' where weekday=2"""
			cursor.execute(d2)
			d3=""" update 'maintable' set weekday ='Wednesday' where weekday=3"""
			cursor.execute(d3)
			d4=""" update 'maintable' set weekday ='Thursday' where weekday=4"""
			cursor.execute(d4)
			d5=""" update 'maintable' set weekday ='Friday' where weekday=5"""
			cursor.execute(d5)
			d6=""" update 'maintable' set weekday ='Saturday' where weekday =6"""
			cursor.execute(d6)
			d7=""" update 'maintable' set weekday = 'Sunday' where weekday=7"""
			cursor.execute(d7)
			op=""" select  * from maintable  order by mydate""".format(MyTable)
			cursor.execute(op)
			km=cursor.fetchall()
			dg=pd.DataFrame(km,columns=['reg','name','mytime','mydate','weekday'])
			print(dg)
			co=""" select * from maintable where mydate='2021/05/15' and mytime<>'Absent' """
			cursor.execute(co)
			#print(cursor.fetchall())
			mk=cursor.fetchall()
			pf=pd.DataFrame(mk,columns=['reg','name','mytime','mydate','weekday'])
		#	print(pf)
	
	
			
				
			
	