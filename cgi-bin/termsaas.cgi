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
emailid="piyushkumar"
uspasswd="ppp"
form = cgi.FieldStorage()  # data store in form var come from html
soft=form.getvalue("termsoft")  # firstname of client 
print soft
q=commands.getstatusoutput(" sudo cut -d':' -f1 /etc/passwd | grep "+str(id)+emailid)
if q[1]==id+emailid:
	z=0
	pass
else:
	commands.getstatusoutput("sudo useradd  "+str(id)+emailid)
	commands.getstatusoutput("sudo  echo -e '"+uspasswd+"\\n"+uspasswd+"' |sudo -i passwd "+str(id)+emailid)
	z=0
if z==0:
	commands.getstatusoutput("sudo setfacl -m u:"+id+emailid+":7 /usr/bin/"+soft)
	commands.getstatusoutput("sudo -i mkdir -p /cloud/software/termsoft/"+soft+"/"+id)
	commands.getstatusoutput("sudo -i chmod 777 /cloud/software/termsoft/"+soft+"/"+id)
	commands.getstatusoutput("sudo -i touch  /cloud/software/termsoft/"+soft+"/"+id+"/"+id+soft+".py")
	commands.getstatusoutput("sudo -i chmod 777 /cloud/software/termsoft/"+soft+"/"+id+"/"+id+soft+".py") # later to particular user
	p="#!/usr/bin/python2"+"\nimport time \nimport commands"+"\nprint'you must have installed openssh rpm on your pc'"+"\ntime.sleep(4)"+"\ncommands.getstatusoutput('systemctl restart sshd')"+"\n"+"commands.getstatusoutput('ssh -X "+id+emailid+"@192.168.0.2 "+soft.lower()+"') \n"
	fh=open("/cloud/software/termsoft/"+soft+"/"+id+"/"+id+soft+".py", mode="wt")
	fh.write(p)
	fh.close()
	commands.getstatusoutput("sudo -i mkdir -p /softtarfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 755 /softtarfile/"+id)
	commands.getstatusoutput("sudo cp /cloud/software/termsoft/"+soft+"/"+id+"/"+id+soft+".py /softtarfile/"+str(id))
	commands.getstatusoutput("sudo chmod 755 /softtarfile/"+id+"/"+id+soft+".py")
	commands.getstatusoutput("sudo -i mkdir -p /var/www/html/cloud/software/termsoft/"+soft+"tarfile/"+id)
	commands.getstatusoutput("sudo -i chmod 777 /var/www/html/cloud/software/termsoft/"+soft+"tarfile/"+id)
	commands.getstatusoutput("sudo -i tar -cvf /var/www/html/cloud/software/termsoft/"+soft+"tarfile/"+id+"/"+id+soft+".tar  /softtarfile/"+id+"/"+id+soft+".py") #providing client side software 
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/cloud/software/termsoft/"+soft+"tarfile/"+id+"/"+id+soft+".tar"+"\">\n"; 
	print "succesfull"
else:
	print "select software"

