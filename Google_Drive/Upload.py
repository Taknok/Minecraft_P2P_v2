import time


if __name__ == "__main__":
    from generaux import *
    from apiclient.http import MediaFileUpload
else:
    from .generaux import *
    from .apiclient.http import MediaFileUpload


def Upload(path_file, title,in_folder = False, exception = False):
    print("Debut de l'upload...")
    
    while upload_in_course() and not exception: #si le drive est en cour d'édition on attend
        time.sleep(5)
    
    
    FILENAME = path_file
    
    credentials = credentials_creator()

    drive_service = build_service(credentials)
    

    # Use 'drive_service' for all of the API calls
    # Insert a file

    media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
    body = {
        'title': title,
        'mimeType': 'text/plain'
    }
    

        
    
    drive_service.files().insert(body=body, media_body=media_body).execute()
    
    
    print("Upload Fini !")


"""


def check_existence_of(object_to_check):
    """
    #Check l'existence du fichier dans la drive
"""
    #on recupère les fichiers existant dans le drive
    credentials = credentials_creator()
    service = build_service(credentials)
    fichiers_dans_le_drive = retrieve_all_files(service)
    
    for i in range(len(fichiers_dans_le_drive)): #on test les objets dans le drive
        title_on_drive = fichiers_dans_le_drive[i]['title']
        if object_to_check == title_on_drive :
            return True
    
    return False


def find_folderid(file_name):
    credentials = credentials_creator()
    service = build_service(credentials)
    fichiers_dans_le_drive = retrieve_all_files(service)
    for i in range(len(fichiers_dans_le_drive)):
        if file_name == fichiers_dans_le_drive[i]['title'] and fichiers_dans_le_drive:
            return fichiers_dans_le_drive[i]['id']
    
    return False
    
    

def Create_folder(title, in_folder == False):
    """
    #creer un dossier dans le drive
"""
    credentials = credentials_creator()
    service = build_service(credentials)
    body = {
      'title': title,
      'mimeType': 'application/vnd.google-apps.folder',
}
    if in_folder != False:
        folder_id = find_folderid()
        body['parents'] = [{'id': folder_id}]
        
    service.files().insert(body=body).execute()



def Upload_folder(path_folder, title,exception = False):
    print("Debut de l'upload du dossier...")
    
    for root, dirs, files in os.walk(path_folder):
        
        for directory in dirs:
            if check_existence_of(directory) == False :
                Create_folder(directory)
        
        for file in files:
            relative_file = os.path.relpath(root,path_of_file_to_save) + "\\" + file
            zipf.write(os.path.join(root, file), relative_file)
    print("Fini !")
    
    
    while upload_in_course() and not exception: #si le drive est en cour d'édition on attend
        time.sleep(5)
    
    
    FILENAME = path_folder
    
    credentials = credentials_creator()

    drive_service = build_service(credentials)
    

    # Use 'drive_service' for all of the API calls
    # Insert a file

    media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
    body = {
        'title': title,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    
    folder_id = "0B_iCMJDnGmmtfjA2UHlUeENiMXlQWW53bmNLbkQ5MlNKYVRnM0NYQjNzbHVGN0RnUW1kX1k"
    if folder != False :
        folder_id = find_folderid()
        body['parents'] = [{'id': folder_id}]
    
    
    drive_service.files().insert(body=body, media_body=media_body).execute()
    
    
    print("Upload dossier Fini !")
"""

if __name__ == "__main__":
    import os,pdb
    Upload(os.path.dirname(os.path.abspath(__file__)) + '\\document_test.txt', 'Fichier test')
    
