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
osname=form.getvalue("osname")  # firstname of client
osno=form.getvalue("osno")
print osname 
print osno
commands.getstatusoutput(" sudo virsh start "+osname)
commands.getstatusoutput("sudo  chmod 777 /websockify-master/websockify.py")
commands.getstatusoutput("sudo /websockify-master/websockify.py -D 192.168.0.2:100{0}      192.168.0.2:59{0}".format(osno))
print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/galary.html\">\n";
