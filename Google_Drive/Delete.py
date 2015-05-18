# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 00:43:56 2015

@author: Paul
"""
import time


if __name__ == "__main__":
    from generaux import *
else:
    from .generaux import *

def Delete(title, exception = False):
    
    while upload_in_course() and not exception : #si le drive est en cour d'édition on attend
        time.sleep(5)
    
    credentials = credentials_creator()
    service = build_service(credentials)
    
    fichiers_dans_le_drive = retrieve_all_files(service)
    
    for i in range(len(fichiers_dans_le_drive)):
        if fichiers_dans_le_drive[i]["title"] == title :
            file_id = fichiers_dans_le_drive[i]["id"]
    service.files().delete(fileId=file_id).execute()
    print("Suppression de " + title +" effectuée !")

if __name__ == "__main__":
    Delete("Fichier test")