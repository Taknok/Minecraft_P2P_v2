# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:50:40 2015

@author: Paul
"""
import time


if __name__ == "__main__":
    from generaux import *
else:
    from .generaux import *


def Download(title,path_and_name_save_file, exception = False):
    print("Telechargement")
    
    while upload_in_course() and not exception : #si le drive est en cour d'édition on attend
        time.sleep(5)
    
    credentials = credentials_creator()
    service = build_service(credentials)
    
    fichiers_dans_le_drive = retrieve_all_files(service)
    for i in range(len(fichiers_dans_le_drive)):
        if fichiers_dans_le_drive[i]["title"] == title :
            file_id = fichiers_dans_le_drive[i]["id"] #on recupere l'id du ficher
    
    drive_file = print_file(service,file_id) #on recupère les metadata qui ont entre autre le lien de telechargement du fichier
    download_file(service,drive_file,path_and_name_save_file)
    print("Telechargement effectue !")
      
if __name__ == "__main__":
    Download("Fichier test","retour_test.txt")