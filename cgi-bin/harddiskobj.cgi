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
id="1"
emailid="piyushkumar"
sampasswd="ppp"
uspasswd="ppp"
form = cgi.FieldStorage()  # data store in form var come from html
staas=form.getvalue("staasmethod")  # firstname of client
hddname=form.getvalue("hddname") 
rangestaashdd=form.getvalue("rangestaashdd")
if staas=="nfs":
	commands.getstatusoutput("sudo -i lvcreate --size " + str(rangestaashdd) + "G --name "+str(id)+""+hddname+"nfs  piycl")   #user folder create later in place of piyush
	commands.getstatusoutput("sudo -i mkfs.ext4 /dev/piycl/"+str(id)+hddname+"nfs")
	commands.getstatusoutput("sudo -i mkdir -p /cloud/object/nfs/"+str(id)+hddname+"nfs") #provide permission for write to user	
	commands.getstatusoutput("sudo -i  mount /dev/piycl/"+str(id)+hddname+"nfs  /cloud/object/nfs/"+str(id)+hddname+"nfs")             
	commands.getstatusoutput("sudo -i chmod 777 /etc/exports") # later to particular user
	fh=open("/etc/exports", mode="at")
	fh.write("/cloud/object/nfs/"+str(id)+hddname+"nfs *(rw,no_root_squash)" + "\n")
	fh.close()
	commands.getstatusoutput("sudo -i mkdir -p /cloud/object/nfsfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 777 /cloud/object/nfsfile/"+str(id))
	commands.getstatusoutput("sudo -i touch  /cloud/object/nfsfile/"+str(id)+"/"+str(id)+hddname+".py")
	commands.getstatusoutput("sudo -i chmod 777 /cloud/object/nfsfile/"+str(id)+"/"+str(id)+hddname+".py") # later to particular user
	p='#!/usr/bin/python2'+"\nimport time \nimport commands"+"\ncommands.getstatusoutput('systemctl restart nfs')"+" \ncommands.getstatusoutput('mkdir /media/"+hddname+"')"+"\n"+"commands.getstatusoutput('mount 192.168.0.2:/cloud/object/nfs/"+str(id)+hddname+"nfs  /media/"+hddname+"') \n"+"print 'Wait a second to mount'\n"+"time.sleep(5)"
	fh=open('/cloud/object/nfsfile/'+str(id)+"/"+str(id)+hddname+".py", mode="wt")
	fh.write(p)
	fh.close()
	commands.getstatusoutput("sudo -i mkdir -p /tarfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 777 /tarfile/"+str(id))
	commands.getstatusoutput("sudo cp /cloud/object/nfsfile/"+str(id)+"/"+id+hddname+".py /tarfile/"+str(id))
	commands.getstatusoutput("sudo chmod 777 /tarfile/"+str(id)+"/"+str(id)+hddname+".py")
	commands.getstatusoutput("sudo -i mkdir -p /var/www/html/cloud/object/nfstarfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 777 /var/www/html/cloud/object/nfstarfile/"+str(id))
	commands.getstatusoutput("sudo -i tar -cvf /var/www/html/cloud/object/nfstarfile/"+str(id)+"/"+str(id)+hddname+".tar  /tarfile/"+str(id)+"/"+str(id)+hddname+".py") #providing client side software s
	print "succesful"
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/cloud/object/nfstarfile/"+str(id)+"/"+str(id)+hddname+".tar"+"\">\n";
elif staas=="sshfs":
	q=commands.getstatusoutput(" sudo cut -d':' -f1 /etc/passwd | grep "+str(id)+emailid)
	if q[1]==str(id)+emailid:
		z=0
		pass
	else:
		commands.getstatusoutput("sudo useradd  "+str(id)+emailid)
		commands.getstatusoutput("sudo  echo -e '"+uspasswd+"\\n"+uspasswd+"' |sudo -i passwd "+str(id)+emailid)
		z=0
	if z==0:
		commands.getstatusoutput("sudo setfacl -m u:"+str(id)+emailid+":7 /usr/bin/ssh")
		commands.getstatusoutput("sudo -i lvcreate --size " + str(rangestaashdd) + "G --name "+str(id)+hddname+"sshfs  piycl")   #user folder create later in place of piyush
		commands.getstatusoutput("sudo -i mkfs.ext4 /dev/piycl/"+str(id)+hddname+"sshfs")
		commands.getstatusoutput("sudo -i mkdir -p /cloud/object/sshfs/"+str(id)+hddname+"sshfs") #provide permission for write to user
		commands.getstatusoutput("sudo -i  mount /dev/piycl/"+str(id)+hddname+"sshfs  /cloud/object/sshfs/"+str(id)+hddname+"sshfs")             
		commands.getstatusoutput("sudo -i mkdir -p /cloud/object/sshfsfile/"+str(id))
		commands.getstatusoutput("sudo -i chmod 777 /cloud/object/sshfsfile/"+str(id))
		commands.getstatusoutput("sudo -i touch  /cloud/object/sshfsfile/"+str(id)+"/"+str(id)+hddname+".py")
		commands.getstatusoutput("sudo -i chmod 777 /cloud/object/sshfsfile/"+str(id)+"/"+str(id)+hddname+".py") # later to particular user
		p='#!/usr/bin/python2'+"\nimport time \nimport commands"+" \ncommands.getstatusoutput('mkdir /media/"+hddname+"')"+"\n"+"commands.getstatusoutput('sshfs "+str(id)+emailid+"@192.168.0.2:/cloud/object/sshfs/"+str(id)+hddname+"sshfs  /media/"+hddname+"') \n"+"print 'Wait a second to mount'\n"+"time.sleep(5)"
		fh=open('/cloud/object/sshfsfile/'+str(id)+"/"+str(id)+hddname+".py", mode="wt")
		fh.write(p)
		fh.close()
		commands.getstatusoutput("sudo -i mkdir -p /tarfile/"+str(id))
		commands.getstatusoutput("sudo -i chmod 777 /tarfile/"+str(id))
		commands.getstatusoutput("sudo cp /cloud/object/sshfsfile/"+str(id)+"/"+str(id)+hddname+".py /tarfile/"+str(id))
		commands.getstatusoutput("sudo chmod 777 /tarfile/"+str(id)+"/"+str(id)+hddname+".py")
		commands.getstatusoutput("sudo -i mkdir -p /var/www/html/cloud/object/sshfstarfile/"+str(id))
		commands.getstatusoutput("sudo -i chmod 777 /var/www/html/cloud/object/sshfstarfile/"+str(id))
		commands.getstatusoutput("sudo -i tar -cvf /var/www/html/cloud/object/sshfstarfile/"+str(id)+"/"+str(id)+hddname+".tar  /tarfile/"+str(id)+"/"+str(id)+hddname+".py") #providing client side software 
		print "succesful"
		print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/cloud/object/sshfstarfile/"+str(id)+"/"+str(id)+hddname+".tar"+"\">\n";
elif staas=="samba":
	commands.getstatusoutput("sudo -i lvcreate --size " + str(rangestaashdd) + "G --name "+str(id)+emailid+"sam  piyusambacl")   #user folder create later in place of piyush
	commands.getstatusoutput("sudo -i mkfs.ext4 /dev/piyusambacl/"+str(id)+emailid+"sam")
	commands.getstatusoutput("sudo -i mkdir -p /cloud/object/samba/"+str(id)+emailid+"sam") #provide permission for write to user
	commands.getstatusoutput("sudo  chmod o+rw /cloud/object/samba/"+str(id)+emailid+"sam")
	commands.getstatusoutput("sudo  mount /dev/piyusambacl/"+str(id)+emailid+"sam  /cloud/object/samba/"+str(id)+emailid+"sam")             
	commands.getstatusoutput("sudo -i useradd -s /sbin/nologin "+str(id)+emailid+"sam")
	commands.getstatusoutput("sudo  echo -e '"+sampasswd+"\\n"+sampasswd+"' |sudo smbpasswd -a "+str(id)+emailid+"sam")
	commands.getstatusoutput("sudo -i chmod 777 /etc/samba/smb.conf") # later to particular user
	fh=open("/etc/samba/smb.conf", mode="at")
	fh.seek(66)
	fh.write("["+str(id)+emailid+"] \npath=/cloud/object/samba/"+str(id)+emailid+"sam"+"\n#hosts allow =*\nwritable=yes\nvalid users="+str(id)+emailid+"sam\n browseable=yes\n")
	fh.close()
	commands.getstatusoutput("sudo systemctl restart smb")
	commands.getstatusoutput("sudo -i mkdir -p /cloud/object/sambafile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 777 /cloud/object/sambafile/"+str(id))
	commands.getstatusoutput("sudo -i touch  /cloud/object/sambafile/"+str(id)+"/"+str(id)+emailid+".py")
	commands.getstatusoutput("sudo -i chmod 777 /cloud/object/sambafile/"+str(id)+"/"+str(id)+emailid+".py") # later to particular user
	p='#!/usr/bin/python2'+"\nimport time \nimport commands"+"\nprint 'Install first cifs-utils and samba-client for linux user'"+"\ntime.sleep(5)"+" \ncommands.getstatusoutput('mkdir /media/"+hddname+"')"+"\ncommands.getstatusoutput('mount -o username="+str(id)+emailid+"sam //192.168.0.2/"+str(id)+emailid+"  /media/"+hddname+"') \n"+"print 'Wait a second to mount'\n"+"time.sleep(5)"
	fh=open('/cloud/object/sambafile/'+str(id)+"/"+str(id)+emailid+".py", mode="wt")
	fh.write(p)
	fh.close()
	commands.getstatusoutput("sudo -i mkdir -p /tarfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 755 /tarfile/"+str(id))
	commands.getstatusoutput("sudo cp /cloud/object/sambafile/"+str(id)+"/"+str(id)+emailid+".py /tarfile/"+str(id))
	commands.getstatusoutput("sudo chmod 755 /tarfile/"+str(id)+"/"+str(id)+emailid+".py")
	commands.getstatusoutput("sudo -i mkdir -p /var/www/html/cloud/object/sambatarfile/"+str(id))
	commands.getstatusoutput("sudo -i chmod 777 /var/www/html/cloud/object/sambatarfile/"+str(id))
	commands.getstatusoutput("sudo -i tar -cvf /var/www/html/cloud/object/sambatarfile/"+str(id)+"/"+str(id)+emailid+".tar  /tarfile/"+str(id)+"/"+str(id)+emailid+".py") #providing client side software 
	print "succesful"
	print "<META HTTP-EQUIV=REFRESH CONTENT=\"0;URL=http://192.168.0.2/cloud/object/sambatarfile/"+str(id)+"/"+str(id)+emailid+".tar"+"\">\n";
else:
	print "not select the choice "
