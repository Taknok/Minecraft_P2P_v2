# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:40:46 2015

@author: Paul
"""



from Google_Drive import *
#import Google_Drive

from Gestion_Fichier import *
import os, shutil
import pdb
chemin = os.path.dirname(os.path.realpath(__file__))






login()
Download("Online-P2Pconfiguration", chemin + "\\Online-P2Pconfiguration.txt")


P2Pconf = open("Old-P2Pconfiguration.txt","r+")
P2Pconfiguration = P2Pconf.read()
P2Pconf.close()

Online_P2Pconf = open("Online-P2Pconfiguration.txt","r+")
Online_P2Pconfiguration = Online_P2Pconf.read()
Online_P2Pconf.close()

Maconf = open("Maconfiguration.txt","r+")
Maconfiguration = Maconf.read()
Maconf.close()



Online = list_parameter(Online_P2Pconfiguration)
Local = list_parameter(P2Pconfiguration)
Conf = list_parameter(Maconfiguration)

creator_launcher_minecraft(Conf)
os.system("start_minecraft.bat")



"""pourra se mettre dans update map"""
if Local["mapversion"] < Online["mapversion"] : #si la version en ligne est plus recente, on la telecharge
    Download("Map.zip",chemin + "\\Temp\\Map.zip")
    shutil.rmtree(Conf["pathserver"] + "\\world")
    os.mkdir(Conf["pathserver"] + "\\world")
    unzip(Conf["pathserver"] + "\\world",chemin + "\\Temp\\Map.zip")
    os.remove(chemin + "\\Temp\\Map.zip")

if active(Online):
    print("Ip du serveur : " + Online[Online["activehost"]]["ip"])

else:
    creator_launcher_server(Conf)
    os.system("start_server.bat")
    
    hosting(True,Online_P2Pconfiguration,Conf)
    
    

    
    Delete("Online-P2Pconfiguration.txt")
    Upload(chemin + "\\Online-P2Pconfiguration.txt","Online-P2Pconfiguration.txt")
    
    saisie = input("press enter to exit\n")
    
    Upload(chemin + "\\__init__.py","Loading")
    
    hosting(False,Online_P2Pconfiguration,Conf,mapversion = Online["mapversion"])
    zipdir(Conf["pathserver"] + "\\world", chemin +"\\Temp\\Map.zip")
    
    Delete("Online-P2Pconfiguration.txt", exception = True)
    Delete("Map.zip",exception = True)
    Upload(chemin + "\\Online-P2Pconfiguration.txt","Online-P2Pconfiguration.txt",exception = True)
    print("Map : ")
    Upload(chemin + "\\Temp\\Map.zip", "Map.zip",exception = True)
    os.remove(chemin + "\\Temp\\Map.zip")
    Delete("Loading",exception = True)
    os.remove(chemin + "\\Old-P2Pconfiguration.txt")
    os.rename(chemin + "\\Online-P2Pconfiguration.txt",chemin + "\\Old-P2Pconfiguration.txt")
    