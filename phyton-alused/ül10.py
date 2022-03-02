#Peedu Erik Pajo
#Ülesanne 10
# 28.03.2022

import re

fh = open("kood.txt")
for line in fh:
     if re.search("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", line):
         print(line,end= '')
    
kh = open("kood.txt")
for line in kh:
     if re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z]).*$", line):
         print(line,end= '')
    