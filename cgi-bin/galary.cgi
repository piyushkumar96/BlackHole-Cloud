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
createos=form.getvalue("yes")  # firstname of client 

if createos=="yes":
	string_to_check = "<p></p>"
	string_to_add = '<div  class="col-md-4 galary-list-gd"><iframe class="galary-list-frame clr-frame os-1"><div class="clearfix"> </div></iframe><a title="Start" href="http://www.google.com" color="red"><span class="fa-stack fa-2x"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-plug fa-stack-1x"></i></span></a><a  title="Play" href="http://www.google.com" color="red"><span class="fa-stack fa-2x"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-play-circle fa-stack-1x"></i></span></a><a title="Pause" href="http://www.google.com" color="red"><span class="fa-stack fa-2x"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-pause-circle fa-stack-1x"></i></span></a><a title="Power Off" href="http://www.google.com" color="red"><span class="fa-stack fa-2x"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-power-off fa-stack-1x"></i></span></a><a title="Fullscreen" data-toggle="modal" data-target="#myModal" color="red"><span class="fa-stack fa-2x"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-arrows-alt fa-stack-1x"></i></span></a><div  class="modal fade  " id="myModal" tabindex="-1" role="dialog"  aria-labelledby="myModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button><h4 class="modal-title" id="myModalLabel">REDHAT</h4></div><iframe  src="http://192.168.0.2/vnc/?host=192.168.0.2&port=1222"  width="100%" height="100%" >div class="clearfix"> </div></iframe></div></div></div></div>\n<p></p>'
	with open("/var/www/html/htmlpiyush/galary.html", 'r+') as file_to_write:
		lines = file_to_write.readlines()
		file_to_write.seek(0)
		file_to_write.truncate()
		for line in lines:
			if line.startswith(string_to_check):
				line = string_to_add + "\n"
			file_to_write.write(line)
	file_to_write.close()
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/galary.html\">\n";