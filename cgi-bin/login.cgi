#!/usr/bin/python2
import cgi  # common gateway interface 
import cgitb   #trace back for troubleshooting
import commands
import mysql.connector as mariadb
import time

cgitb.enable()
print "content-type:text/html"  # content run in browser must in html
# header is close  python 

form = cgi.FieldStorage()  # data store in form var come from html
emailid=form.getvalue("emailid") #store value whose name is rahul
password=form.getvalue("password")
commands.getstatusoutput("sudo -i systemctl restart mariadb")
mariadb_connection = mariadb.connect(user='root', password='piyushmdb', database='piyucloud')
cursor = mariadb_connection.cursor()
#retrieving information
u=[]
cursor.execute("SELECT EMAILID_CL FROM CLIENTS")
r=cursor.fetchall();
for a in r:
	for b in a:
		u.append(str(b))
y=[]
id=[]
k=emailid in u
if k==True: 
    cursor.execute('SELECT ID,PASSWD_CL FROM CLIENTS WHERE EMAILID_CL="%s";' % (emailid))
    w=cursor.fetchall();
    for  a in w:
    	for b in a:
    		y.append(str(b))    
	h=password in y[1]
	id=y[0]
    if h==True:
    	print "Set-Cookie:piyush="+id+emailid+";Path=/;\r\n"
    	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/index.html\">\n";
    else:
    	print ""
    	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/passwordwrong.html\">\n";
else:
	print ""
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/clientexist.html\">\n";
mariadb_connection.close()
print ""
