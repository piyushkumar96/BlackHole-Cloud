#!/usr/bin/python
#common gateway interface
import cgi  # common gateway interface 
import cgitb   #trace back for troubleshooting
import commands
import mysql.connector as mariadb
import string
cgitb.enable()
print "content-type:text/html"  # content run in browser must in html
print ""                        # header is close  python 

form = cgi.FieldStorage()  # data store in form var come from html
firstname=form.getvalue("firstname")  # firstname of client 
lastname=form.getvalue("lastname")    # lastname of client 
password=form.getvalue("password")    # password of client 
gender=form.getvalue("gender")
if gender=='male':
    gend='M'
else:
	gend='F'        # gender of client  
dob=form.getvalue("dob")              # dob of client     
emailid=form.getvalue("emailid")      # emailid of client 
phoneno=form.getvalue("phoneno")      # phoneno of client 
profilepic=form.getvalue("profilepic")      # profilepic of client 

commands.getstatusoutput("sudo -i systemctl restart mariadb")
mariadb_connection = mariadb.connect(user='root', password='piyushmdb', database='piyucloud')
cursor = mariadb_connection.cursor()
p=[]
cursor.execute("SELECT EMAILID_CL FROM CLIENTS")
r=cursor.fetchall()
for a in r:
	for b in a:
		p.append(str(b))
		
if emailid in p:
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/clientexist.html\">\n";
else:    
	cursor.execute("INSERT INTO CLIENTS (FIRST_NAME,LAST_NAME,PASSWD_CL,GENDER_CL,DOB_CL,EMAILID_CL,PHONENO_CL) VALUES (%s,%s,%s,%s,%s,%s,%s)",(firstname,lastname,password,gend,dob,emailid,phoneno))         
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/login.html\">\n";
			
mariadb_connection.commit()

'''print "The last inserted id was: ", cursor.lastrowid 
'''
mariadb_connection.close()
	
