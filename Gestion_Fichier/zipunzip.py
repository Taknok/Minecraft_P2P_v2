# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 01:10:44 2015

@author: Paul
"""

import zipfile, os



def zipdir(path_of_file_to_save, path_output_and_name_zipfile):
    print("Creation du zip...")
    zipf = zipfile.ZipFile(path_output_and_name_zipfile,"w")
    for root, dirs, files in os.walk(path_of_file_to_save):

        for file in files:
            relative_file = os.path.relpath(root,path_of_file_to_save) + "\\" + file
            zipf.write(os.path.join(root, file), relative_file)
    print("Fini !")
    zipf.close()



def unzip(path_to_extract,path_and_name_zip_file):
    print("Unzipage...")
    z = zipfile.ZipFile(path_and_name_zip_file)
    z.extractall(path_to_extract)
    print("Fini !")


if __name__ == "__main__":
    zipdir("D:\Desktop\Paul\Developpement\Python\Spyder_Project\Minecraft_P2P\Google_Drive","D:\Desktop\Paul\Developpement\Python\Spyder_Project\Minecraft_P2P\\Gestion_Fichier\\test.zip")
    unzip("D:\Desktop\Paul\Developpement\Python\Spyder_Project\Minecraft_P2P\\Gestion_Fichier","D:\Desktop\Paul\Developpement\Python\Spyder_Project\Minecraft_P2P\\Gestion_Fichier\\test.zip")