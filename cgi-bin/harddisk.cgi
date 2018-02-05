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
staas=form.getvalue("staas")  # firstname of client 
if staas=="objstaas":
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/harddiskobj.html\">\n";
else:
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/harddiskblk.html\">\n";


	
