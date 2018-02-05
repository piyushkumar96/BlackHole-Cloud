#!/usr/bin/python
#common gateway interface
import cgi  # common gateway interface 
import cgitb   #trace back for troubleshooting
import commands
import mysql.connector as mariadb
import string
import sys
import time
cgitb.enable()
print "content-type:text/html"  # content run in browser must in html
print ""                        # header is close  python 
id="1"
emailid="piyushkumar"
sampasswd="ppp"
uspasswd="ppp"
form = cgi.FieldStorage()  # data store in form var come from html
staas=form.getvalue("staasmethod")  # firstname of client
hddname=form.getvalue("hddname") 
rangestaashdd=form.getvalue("rangestaashdd")
if staas=="iscsi":
	commands.getstatusoutput("sudo -i lvcreate --size " + str(rangestaashdd) + "G --name "+str(id)+hddname+"iscsi  piycl")   #user folder create later in place of piyush
	commands.getstatusoutput("sudo touch /etc/tgt/conf.d/"+str(id)+emailid+"iscsi.conf") 
	commands.getstatusoutput("sudo -i chmod 777 /etc/tgt/conf.d/"+str(id)+emailid+"iscsi.conf") 
	fh=open("/etc/tgt/conf.d/"+str(id)+emailid+"iscsi.conf", mode="at")
	fh.write("<target my"+str(id)+hddname+"iscsi>\nbacking-store /dev/piycl/"+str(id)+hddname+"iscsi \n</target>" + "\n")
	fh.close()
	#commands.getstatusoutput("sudo -i  systemctl restart tgtd")
	time.sleep(5)
	commands.getstatusoutput("sudo -i mkdir -p /cloud/block/iscsifile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 777 /cloud/block/iscsifile/"+str(id))
	commands.getstatusoutput("sudo -i touch  /cloud/block/iscsifile/"+str(id)+"/"+str(id)+hddname+".py")
	commands.getstatusoutput("sudo -i chmod 777 /cloud/block/iscsifile/"+str(id)+"/"+str(id)+hddname+".py") # later to particular user
	p='#!/usr/bin/python2'+"\nimport time \nimport sys \nimport commands"+"\nprint 'Wait few second until disk will mount' "+"\ntime.sleep(10)"+"\nprint 'Raw Hardisk is successfull mounted on your pc' "+" \ncommands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.0.2 --discover')\n"+"\nsys.stdout.write('Enter (login) keyword to login ')"+"\n"+"logi=raw_input()"+"\ncommands.getstatusoutput('iscsiadm --mode node --targetname my"+str(id)+hddname+"iscsi --portal 192.168.0.2:3260 --'+logi)"+" \nsys.stdout.write('you are loged in now you can use raw hardisk  :')"+"\nsys.stdout.write(' If you want To logout then enter (logout) :')\n"+"logo=raw_input()\n"+"commands.getstatusoutput('iscsiadm --mode node --targetname my"+str(id)+hddname+"iscsi --portal 192.168.0.2:3260 --'+logo)\n"+"sys.stdout.write(' you are loged out :::::::::::::::::::::::')"+"\ntime.sleep(5)\n"
	fh=open('/cloud/block/iscsifile/'+str(id)+"/"+str(id)+hddname+".py", mode="wt")
	fh.write(p)
	fh.close()
	commands.getstatusoutput("sudo -i mkdir -p /tarfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 755 /tarfile/"+str(id))
	commands.getstatusoutput("sudo cp /cloud/block/iscsifile/"+str(id)+"/"+str(id)+hddname+".py /tarfile/"+str(id))
	commands.getstatusoutput("sudo chmod 755 /tarfile/"+str(id)+"/"+str(id)+hddname+".py")
	commands.getstatusoutput("sudo -i mkdir -p /var/www/html/cloud/block/iscsitarfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 777 /var/www/html/cloud/block/iscsitarfile/"+str(id))
	commands.getstatusoutput("sudo -i tar -cvf /var/www/html/cloud/block/iscsitarfile/"+str(id)+"/"+str(id)+hddname+".tar  /tarfile/"+str(id)+"/"+str(id)+hddname+".py") #providing client side software
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/cloud/block/iscsitarfile/"+str(id)+"/"+str(id)+hddname+".tar"+"\">\n"; 
	print "succesful"
else:
	print "select option"
