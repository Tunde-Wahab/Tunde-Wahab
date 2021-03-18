from sqlite3 import dbapi2 as sqlite3
import re,time
c=time.asctime()   
x= int(input('enter your regno:'))
y= str(input('enter your name:')).capitalize()
#k=int(input('enter the no to search for:'))
a,d=(int,re.findall(r'\d+',c))
u=(c[4:7])
l=(c[0:3])
#print(l)
#print(c)
p=('%s%s%s%s%s' %(d[0],'/',u,'/',d[4]))
#print(p)
h=('%s%s%s%s%s'%(d[1],':',d[2],':',d[3]))
MyTable=d[2]
sqlitecn=sqlite3.connect('strdcb_db')
cursor=sqlitecn.cursor()
cret=""" create table if not exists ss3able(matric integer primary key unique,name text,mytime text); """
cursor.execute(cret)
inser=""" insert into ss3able(matric,name)
values(?,?); """
data=(x,y)
cursor.execute(inser,data)
sel=""" select * from ss3able"""
cursor.execute(sel)
c=cursor.fetchall()
#print(c)
cv=""" create table if not exists '{}' as select matric,name from ss3able; """.format(MyTable)
cursor.execute(cv)
sqlitecn.commit()
mytri=""" create trigger if not exists mytrig after insert on ss3able
begin
insert into '{}'(matric,name) select * from ss3able;end; """.format(MyTable)
cursor.execute(mytri)
sqlitecn.commit()
newtrig= """create trigger if not exists newr before update on '{}'
when new.matric=old.matric
begin
 update '{}' set mytime=datetime('now','localtime');end; """.format(MyTable,MyTable)
ct=""" create view if not exists myview(Nmatric,Nname,Nmytime)
 As
     select
         matric,name,mytime
       from 
               ss3able;"""
cursor.execute(ct)
sqlitecn.commit()
ret=""" create trigger if not exists mytrig instead of insert on myview
begin
insert into ss3able(matric,name) values(new.matric,new.name,new.mytime);end; """
cursor.execute(ret)
sqlitecn.commit()
jk=""" update ss3able set mytime=datetime('now','localtime') where matric='{}' """.format(x)
cursor.execute(jk)
sqlitecn.commit()
gt="""select * from ss3able"""
cursor.execute(gt)
gd=cursor.fetchall()
print(gd)