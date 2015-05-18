# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:39:10 2015

@author: Paul
"""
import os
import zipfile
import httplib2



    
def unzip(path_to_extract,path_and_name_zip_file):
    print("Unzipage...")
    z = zipfile.ZipFile(path_and_name_zip_file)
    z.extractall(path_to_extract)
    print("Fini !")


def ma_conf():
    file = open("Maconfiguarion.txt","w")
    file.write("""<local>Your pseudo here</local>
<pathserver>the path to the server launcher folder</pathserver>
<minecraft>the path to you minecraft launcher</minecraft>""")
    file.close()



def old_conf():
    file = open("Old-P2Pconfiguration.txt","w")
    file.write("""<mapversion>0000-00-00-00-00</mapversion>
<lasthost>Your pseudo here</lasthost>
<activehost>No</activehost>
<player>
	<name>Your pseudo here</name>
	<ip>Your ip adress here</ip>
</player>
<player>
	<name>Other player pseudo</name>
	<ip>Other player ip adress</ip>
</player>""")
    file.close()



chemin = os.path.dirname(os.path.realpath(__file__))
login()
Download("Install.zip",chemin + "\\Install.zip")
unzip(chemin,chemin + "\\Install.zip")
ma_conf()
old_conf()
os.remove("Install.zip")