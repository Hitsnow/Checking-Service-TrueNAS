import tkinter
from tkinter import messagebox
import os
import reboot_domotique
from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()

def ping(ip) :
    stream = os.popen('ping -c 2 {}'.format(ip)) 
    output = stream.read() 
  
    if '0 packets received' in output: 
        print('IP unreachable') 
        status = "ERREUR"
    else:
        print('IP reachable') 
        status = "OK"
    return status


def ssh(cmd,ip,user) :
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(ip, username=user,password="xxxx")
    stdin, stdout, stderr = client.exec_command(cmd)
    retour = stdout.read()
    stdin.close()
    stdout.close()
    stderr.close()
    client.close()
    return retour