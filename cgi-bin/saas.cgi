#!/usr/bin/python
#common gateway interface
import cgi  # common gateway interface 
import cgitb   #trace back for troubleshooting
import commands
import mysql.connector as mariadb
import string
cgitb.enable()
print "content-type:text/html"  # content run in browser must in html
print ""                       # header is close  python 
id="1"
emailid="piyushkumar2"
form = cgi.FieldStorage()  # data store in form var come from html
soft=form.getvalue("software")  # firstname of client 
print soft

'''commands.getstatusoutput("sudo -i systemctl restart mariadb")
mariadb_connection = mariadb.connect(user='root', password='piyushmdb', database='piyucloud')
cursor = mariadb_connection.cursor()
cursor.execute("SELECT XMLFLNO,UUIDNO,PORTNO,MACADD,COUNT,PROKPORTNO FROM XMLINFO WHERE XMLFLNO=(SELECT MAX(XMLFLNO) FROM XMLINFO)")
p=[]
h=cursor.fetchall()
for a in h:
	for h in a:
		p.append(str(h))
xmlflno=int(p[0])+1
uuidno=int(p[1])+1
portno=int(p[2])+1
macadd=int(p[3])+1
count=int(p[4])
PROKPORTNO=int(p[5])+1
maxram=3388608
print p'''
if soft=="FIREFOX":
	print soft
elif soft=="OPERA"
    print soft
elif soft=="OPERA"
    print soft
elif soft=="OPERA"
    print soft
elif soft=="OPERA"
    print soft
elif soft=="OPERA"
    print soft