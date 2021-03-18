from sqlite3 import dbapi2 as sqlite3
import re,time
c=time.asctime()   
#x= int(input('enter your regno:'))
#y= str(input('enter your name:'))
#k=int(input('enter the no to search for:'))
a,d=(int,re.findall(r'\d+',c))
u=(c[4:7])
l=(c[0:3])
#print(l)
#print(c)
p=('%s%s%s%s%s' %(d[0],'/',u,'/',d[4]))
#print(p)
h=('%s%s%s%s%s'%(d[1],':',d[2],':',d[3]))
MyTable=[2]
#print(h)
sqliteconn = sqlite3.connect('ggpp_db	r')
cursor = sqliteconn.cursor()
treatet_table="""create Table if not exists
ba(matric integer primary key unique,name text,my_time text,my_date text);"""
cursor.execute(treatet_table)
sqliteconn.commit()
print('%s created sucessfully'%(MyTable))
tet="""insert into ba(matric,name)values(matric=0,name='Tunde')"""
cursor.execute(tet)
sqlitconn.commit()
f=cursor.fetchall()
print(f)
db={}
print('welcome to timebook project')
while true:
	print('what do you want to do')
	print('Enter R to [R] egistration,S to [S] earch')
	print('Or enter Q to [Q] uite')
	action= input()
	if action =='R':
		while f !=None:
			x=int(input('Enter your regno:'))
			y=str(input('Enter your name:'))
			cret=""" insert into ba (matric,name)
			values(?,?);"""
			data=(x,y)
			cursor.execute(cret,data)
			sqliteconn.commit()
			g=cursor.fetchall()
			print(g)
			
		