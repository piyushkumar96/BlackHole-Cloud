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
ostype=form.getvalue("os")  # firstname of client 
print ostype
osname=form.getvalue("osname")    # lastname of client 
print osname
osram=form.getvalue("ram")    # password of client 
osram=int(osram)*1024
print osram
oscpu=form.getvalue("cpu")
print oscpu
osharddisk=form.getvalue("harddisk")
osharddisk=int(osharddisk)*1024*1024
print osharddisk
osmethod=form.getvalue("method")
print osmethod
commands.getstatusoutput("sudo -i systemctl restart mariadb")
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
count=int(p[4])+1
prokportno=int(p[5])+1
maxram=3388608
print p
if ostype=="REDHAT":
	commands.getstatusoutput('sudo sed -i "s/rhel7.2_15/rhel7.2_{0}/" /etc/libvirt/qemu/rhel7.2_{0}.xml'.format(xmlflno))
	commands.getstatusoutput('sudo sed -i "s/<uuid>de3f5389-e429-4276-89bd-27ac9cd0ca2a/<uuid>de3f5389-e429-4276-89bd-27ac9cd0ca{0}/" /etc/libvirt/qemu/rhel7.2_{1}.xml'.format(uuidno,xmlflno))
	commands.getstatusoutput('sudo sed -i "s/<memory unit=\'KiB\'>1048576</<memory unit=\'KiB\'>{0}</" /etc/libvirt/qemu/rhel7.2_{1}.xml'.format(maxram,xmlflno))
	commands.getstatusoutput('sudo sed -i "s/<currentMemory unit=\'KiB\'>1048576</<currentMemory unit=\'KiB\'>{0}</" /etc/libvirt/qemu/rhel7.2_{1}.xml'.format(osram,xmlflno))
	commands.getstatusoutput('sudo sed -i "s/<vcpu placement=\'static\'>1</<vcpu placement=\'static\'>{0}</" /etc/libvirt/qemu/rhel7.2_{1}.xml'.format(oscpu,xmlflno))
	commands.getstatusoutput('sudo sed -i "s/<mac address=\'52:54:00:3d:c4:9b\'\/>/<mac address=\'52:54:00:3d:c4:{0}\'\/>/" /etc/libvirt/qemu/rhel7.2_{1}.xml'.format(macadd,xmlflno))
	commands.getstatusoutput('sudo sed -i "s/port=\'5915\'/port=\'{0}\'/" /etc/libvirt/qemu/rhel7.2_{1}.xml'.format(portno,xmlflno))
	commands.getstatusoutput('sudo sed -i "s/domain-rhel7.2_15/domain-rhel7.2_{0}/" //etc/libvirt/qemu/rhel7.2_{0}.xml'.format(xmlflno))
	commands.getstatusoutput('sudo sed -i "s/listen=\'0.0.0.0\'/listen=\'0.0.0.0\'/" /etc/libvirt/qemu/rhel7.2_{0}.xml'.format(xmlflno))
	commands.getstatusoutput('sudo sed -i "s/address=\'0.0.0.0\'/address=\'0.0.0.0\'/" /etc/libvirt/qemu/rhel7.2_{0}.xml'.format(xmlflno))
	commands.getstatusoutput('sudo virsh define /etc/libvirt/qemu/rhel7.2_{0}.xml'.format(xmlflno))
	a=commands.getstatusoutput('sudo virsh start rhel7.2_{0}'.format(xmlflno))
	print a
	if a[0]==0:
		commands.getstatusoutput("sudo  chmod 777 /websockify-master/websockify.py")
		x=commands.getstatusoutput("sudo /websockify-master/websockify.py -D 192.168.0.2:{0}      192.168.0.2:{1}".format(prokportno,portno))
		print x
		brace="{}"
		string_to_check = "<p></p>"
		string_to_add = ('<div  class="col-md-4 galary-list-gd">\n<iframe class="galary-list-frame clr-frame os-1"><div class="clearfix"> </div></iframe>\n\t<form id="startrhel7.2_{0}" action="../cgi-bin/start.cgi" method="post" accept-charset="utf-8" >\n\t\t<input name="osname" value="rhel7.2_{0}" type="hidden"/>\n\t\t<input name="osno" value="{0}" type="hidden"/>\n\t\t<a href="javascript:{2}" onclick="document.getElementById(\'startrhel7.2_{0}\').submit();" title="Start"  color="red"><span class="fa-stack fa-2x" style="float:left;" ><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-plug fa-stack-1x"></i></span>\n\t\t</a>\n\t</form>\n\t<form id="resumerhel7.2_{0}" action="../cgi-bin/resume.cgi" method="post" accept-charset="utf-8" >\n\t\t<input name="osname" value="rhel7.2_{0}" type="hidden"/>\n\t\t<a  href="javascript:{2}" onclick="document.getElementById(\'resumerhel7.2_{0}\').submit();" title="Resume"  color="red"><span class="fa-stack fa-2x" style="float:left;" ><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-play-circle fa-stack-1x"></i></span>\n\t\t</a>\n\t</form>\n\t<form id="suspendrhel7.2_{0}" action="../cgi-bin/suspend.cgi" method="post" accept-charset="utf-8" >\n\t\t<input name="osname" value="rhel7.2_{0}" type="hidden"/>\n\t\t<a  href="javascript:{2}" onclick="document.getElementById(\'suspendrhel7.2_{0}\').submit();" title="Suspend" color="red"><span class="fa-stack fa-2x" style="float:left;"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-pause-circle fa-stack-1x"></i></span>\n\t\t</a>\n\t</form>\n\t<form id="shutdownrhel7.2_{0}" action="../cgi-bin/shutdown.cgi" method="post" accept-charset="utf-8" >\n\t\t<input name="osname" value="rhel7.2_{0}" type="hidden"/>\n\t\t<a  href="javascript:{2}" onclick="document.getElementById(\'shutdownrhel7.2_{0}\').submit();" title="Power Off"  color="red"><span class="fa-stack fa-2x" style="float:left;"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-power-off fa-stack-1x"></i></span>\n\t\t</a>\n\t</form>\n\t<form id="fullscreenrhel7.2_{0}" action="../cgi-bin/fullscreen.cgi" method="post" accept-charset="utf-8" >\n\t\t<input name="osno" value="{0}" type="hidden"/>\n\t\t<a  href="javascript:{2}" onclick="document.getElementById(\'fullscreenrhel7.2_{0}\').submit();" title="Fullscreen" data-toggle="modal" data-target="#myModal" color="red"><span class="fa-stack fa-2x"><i class="fa fa-circle fa-stack-2x icon-background4"></i><i class="fa fa-circle-thin fa-stack-2x icon-background6"></i><i class="fa fa-arrows-alt fa-stack-1x"></i></span>\n\t\t</a>\n\t</form>\n\t<div  class="modal fade  " id="myModal" tabindex="-1" role="dialog"  aria-labelledby="myModalLabel" aria-hidden="true">\n\t\t<div class="modal-dialog">\n\t\t<div class="modal-content">\n\t<div class="modal-header">\n\t\t<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button><h4 class="modal-title" id="myModalLabelrhel7.2_{0}">REDHAT</h4></div>\n\t\t<iframe  src="http://192.168.0.2/vnc/?host=192.168.0.2&port={1}"  width="100%" height="100%" >\n\t<div class="clearfix"> </div>\n\t\t</iframe>\n\t\t</div>\n\t\t</div></div>\n</div>\n\n<p></p>'.format(xmlflno,prokportno,brace))
		with open("/var/www/html/htmlpiyush/galary.html", 'r+') as file_to_write:
			lines = file_to_write.readlines()
			file_to_write.seek(0)
			file_to_write.truncate()
			for line in lines:
				if line.startswith(string_to_check):
					line = string_to_add + "\n"
				file_to_write.write(line)
		file_to_write.close()
		y=cursor.execute("UPDATE XMLINFO SET XMLFLNO="+str(xmlflno) + " ,UUIDNO="+str(uuidno) + " ,PORTNO="+str(portno) + " ,MACADD="+str(macadd) + " ,COUNT="+str(count) + " ,PROKPORTNO="+str(prokportno) )
 		mariadb_connection.commit()
		print "success full"
		print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/htmlpiyush/galary.html\">\n";
elif ostype=="windows":
	pass
else:
	pass
