#!/usr/bin/python3
import re
 
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.groups() : ", matchObj.groups())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


line = "No module named 'aaa'"
matchObj = re.match( r'No module named \'(.*)\'', line)
if matchObj:
   print ("matchObj.group(1) : ", matchObj.group(1))
else:
   print ("No match!!")