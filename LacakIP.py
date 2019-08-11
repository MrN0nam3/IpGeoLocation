#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Jangan DiRecode Tod!!
#Tq Mr.N0N4M3

from os import *
from urllib import *
from time import *



banner = """
                   
|======================[IP GEO LOCATION]=====================|                                                
   _| || |_        
  |_  ..  _|     \033[1;32mAUTHOR  : MR.N0N4M3\033[1;36m
  |_      _|     \033[1;31mContact : 081291126318\033[1;36m
    |_||_|       \033[1;31mMy TEAM : Glaxy Cyber Anonymous\033[1;36m

|==========================[WELCOME]=========================|
"""

print banner
print
target = raw_input("\033[0;34mIp Yang Ingin Di Lacak :\033[1;32m ")
url = "http://ip-api.com/json/" +target
data = urlopen(url).read().decode("utf-8")
data2 = eval(data)
print
print("\033[1;36m[ + ] \033[1;32mMengeCek >>>\033[0m")
print
print "\033[1;36m[ + ] \033[0mAS :\033[1;32m ", str(data2["as"])
print "\033[1;36m[ + ] \033[0mCOUNTRY :\033[1;32m ", str(data2["country"])
print "\033[1;36m[ + ] \033[0mCITY :\033[1;32m ", str(data2["city"])
print "\033[1;36m[ + ] \033[0mCOUNTRY CODE :\033[1;32m ", str(data2["countryCode"])
print "\033[1;36m[ + ] \033[0mISP :\033[1;32m ", str(data2["isp"])
print "\033[1;36m[ + ] \033[0mLATITUDE :\033[1;32m ", str(data2["lat"])
print "\033[1;36m[ + ] \033[0mLONGTITUDE :\033[1;32m ", str(data2["lon"])
print "\033[1;36m[ + ] \033[0mORG :\033[1;32m ", str(data2["org"])
print "\033[1;36m[ + ] \033[0mQUERY :\033[1;32m ", str(data2["query"])
print "\033[1;36m[ $ ] \033[0mREGION :\033[1;32m ", str(data2["region"])
print "\033[1;36m[ + ] \033[0mREGION NAME :\033[1;32m ", str(data2["regionName"])
print "\033[1;36m[ + ] \033[0mTIME ZONE :\033[1;32m ", str(data2["timezone"])
print "\033[1;36m[ + ] \033[0mZIP :\033[1;32m ", str(data2["zip"])
print "\033[1;36m[ + ] \033[0mSTATUS :\033[1;32m ", str(data2["status"])
print "\033[0m"
