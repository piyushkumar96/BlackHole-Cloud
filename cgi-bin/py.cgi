#!/usr/bin/python2
import cgi  # common gateway interface 
import cgitb   #trace back for troubleshooting
import commands

cgitb.enable()

print "content-type:text/html"  # content run in browser must in html
print "" # header is close  python 

form = cgi.FieldStorage()  # data store in form var come from html
hello=form.getvalue("name")   # name of client 
#print hello

print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.google.com\">\n";
'''
#a=commands.getstatusoutput( "sudo " + hello)
a=commands.getstatusoutput( "sudo " + hello)
print a*'''
