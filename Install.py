# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:39:10 2015

@author: Paul
"""
import os
import zipfile
import httplib2
from Google_Drive.apiclient import errors
from Google_Drive.apiclient.discovery import build
from Google_Drive.oauth2client.file import Storage
from Google_Drive.oauth2client.client import OAuth2WebServerFlow



print("Installer l'api drive avec la commande : 'pip install git+https://github.com/enorvelle/GoogleApiPython3x.git'")
os.system("pause")



def credentials_creator():
    storage = Storage('a_credentials_file')
    return storage.get()



def build_service(credentials):
    """
    Creer le service google drive
    utilisation : service = built_service(credentials)
    """
    http = httplib2.Http()
    http = credentials.authorize(http)
    return build('drive', 'v2', http=http)



def login():

    # Copy information from the google page developper
    CLIENT_ID = '1055360985442-0ctghdaasiqd5b6hrak2ksuhigf30640.apps.googleusercontent.com'
    CLIENT_SECRET = 'BOz3lv0HEORunY6JQnQMa44o'
    
    # Check https://developers.google.com/drive/scopes for all available scopes
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
    
    # Redirect URI for installed apps, display on the google page devlopper too
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
    
    credentials = credentials_creator()
    
    # Only attempt to get new credentials if the load failed.
    if not credentials:
    
        # Run through the OAuth flow and retrieve credentials                                                                                 
        flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    
        authorize_url = flow.step1_get_authorize_url()
        print ('Go to the following link in your browser: ' + authorize_url)
        code = input('Enter verification code: ').strip()
    
        credentials = flow.step2_exchange(code)
        storage = Storage('a_credentials_file')
        storage.put(credentials)
    


def retrieve_all_files(service):
    """
    Permet de lister tous les fichiers presents dans le drive, attention aussi ceux dans la corbeille, penser la vider !
    Note : ma fonction Delete(title) le supprime aussi de la poubelle donc pas de pb avec
    utilisation : file_dans_le_drive = retrieve_all_files(service)
    """
    result = []
    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token
            files = service.files().list(**param).execute()
    
            result.extend(files['items'])
            page_token = files.get('nextPageToken')
            if not page_token:
                break
        except errors.HttpError as error:
            print('An error occurred: %s' % error)
            break
    return result



def print_file(service, file_id):
    """
    Permet de recupérer les metadata d'un fichier dans le drive
    """
    try:
        file = service.files().get(fileId=file_id).execute()
        return file
    except errors.HttpError as error:
        print ('An error occurred: %s' % error)



def download_file(service, drive_file,name_save_file):
    """
    Permet de telecharger un fichier lorsque l'on a les entrées
    """
    download_url = drive_file.get('downloadUrl')
    if download_url:
        resp, content = service._http.request(download_url)
        if resp.status == 200:
            file = open(name_save_file, 'wb')
            file.write(content)
        else:
            print('An error occurred: %s' % resp)



def Download(title,path_and_name_save_file):
    print("Telechargement")
    
    credentials = credentials_creator()
    service = build_service(credentials)
    
    fichiers_dans_le_drive = retrieve_all_files(service)
    for i in range(len(fichiers_dans_le_drive)):
        if fichiers_dans_le_drive[i]["title"] == title :
            file_id = fichiers_dans_le_drive[i]["id"] #on recupere l'id du ficher
    
    drive_file = print_file(service,file_id) #on recupère les metadata qui ont entre autre le lien de telechargement du fichier
    download_file(service,drive_file,path_and_name_save_file)
    print("Telechargement effectue !")
    
    
    
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