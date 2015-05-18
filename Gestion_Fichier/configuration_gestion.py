# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:36:04 2015

@author: Paul
"""
import time

def test_parameter(text,parameter):
    """
    Test si le parametre est dans le fichier
    """
    if text.find("<" + parameter + ">") != -1:
        return True
    else :
        return False



def remove_text(text,parameter):
    """
    Retire un parametre
    """
    remove = text[text.find("<" + parameter + ">"):text.find("</" + parameter + ">")+ len(parameter) + 3]
    return text.replace(remove,"")



def value_parameter(text,parameter):
    """
    renvoie la valeur du parametre sour forme de str
    """
    return text[text.find("<" + parameter + ">") + len(parameter) + 2 :text.find("</" + parameter + ">")]


def extract_parameter(text,parameter):
    return text[text.find("<" + parameter + ">") + len(parameter) + 2:text.find("</" + parameter + ">")]




def list_parameter(file):
    List_conf = {}
    List_player_parameter = ["ip","ping"]
    List_of_parameter = ["mapversion","lasthost","pathserver","nameserverfile","activehost","minecraft","local","server_data"]
    for parameter in  List_of_parameter:
        if test_parameter(file,parameter):
            List_conf[parameter] = value_parameter(file,parameter)
    while test_parameter(file,"player"):
        Name = value_parameter(file,"name")
        List_conf[Name] = {}
        info_player = extract_parameter(file,"player")
        for player_parameter in List_player_parameter:
            if test_parameter(info_player,player_parameter):
                List_conf[Name][player_parameter] = value_parameter(info_player,player_parameter)
        
        file = remove_text(file,"player")
            
    return List_conf
    
    

def active(Online):
    if Online["activehost"] != "No":
        return True
    else:
        return False



def creator_launcher_minecraft(Conf):
    file = open("start_minecraft.bat","w")
    file.write("""D:
cd """ + Conf["minecraft"] + """
start FTBLauncher_64bit.exe""")



def creator_launcher_server(Conf):
    adresse = Conf["pathserver"]
    disque = adresse[:adresse.find("\\"):]
    file = open("start_server.bat","w")
    file.write(disque + """
cd """ + adresse + """
start """ + Conf["nameserverfile"])



def hosting(Bool,Online_P2Pconfiguration,Conf,mapversion = None):
    if Bool:
        Text = Online_P2Pconfiguration.replace("""<activehost>No</activehost>""","""<activehost>"""+ Conf["local"] +"""</activehost>""")
        Online_P2Pconf = open("Online-P2Pconfiguration.txt","w")
        Online_P2Pconf.write(Text)
        Online_P2Pconf.close()

    else:
        Text = Online_P2Pconfiguration.replace("""<activehost>"""+ Conf["local"] +"""</activehost>""","""<activehost>No</activehost>""")
        Text = Text.replace("""<mapversion>"""+ mapversion +"""</mapversion>""","""<mapversion>"""+ time.strftime("%Y-%m-%d-%H-%M") +"""</mapversion>""")
        Online_P2Pconf = open("Online-P2Pconfiguration.txt","w")
        Online_P2Pconf.write(Text)
        Online_P2Pconf.close()

def modification_server_info(Conf):
    """
    Modifie les infos dans le fichier minecraft pour que le serveur soit réglé sur l'ip de l'hote
    """
    file = open(Conf["server_data"],"r")
    text = file.read()
    file.close()
    file = open(Conf["server_data"],"w")
    file.write(text)
    file.close()
    