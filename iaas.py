#!/usr/bin/python2

import  cgi
import  cgitb
cgitb.enable()
import  commands
print  "Content-Type: text/html"
print   ""

web_data=cgi.FieldStorage()
#  extracting  os name from html file 
os_name=web_data.getvalue('os')
os_ram=web_data.getvalue('or')
os_cpu=web_data.getvalue('oc')
os_hdd=web_data.getvalue('oh')
os_port=web_data.getvalue('op')

#  print all data
os_launch="sudo virt-install --cdrom /rhel.iso  --ram  "+os_ram+" --vcpu "+os_cpu+" --nodisk --name  "+os_name+" --graphics vnc,listen=0.0.0.0,port="+os_port 

print  commands.getoutput(os_launch)
