



def print_files_in_folder(folder_id):
  credentials = credentials_creator()
  service = build_service(credentials)
  """Print files belonging to a folder.

  Args:
    service: Drive API service instance.
    folder_id: ID of the folder to print files from.
  """
  page_token = None
  while True:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      children = service.children().list(folderId=folder_id, **param).execute()

      for child in children.get('items', []):
          print (child)
        
      page_token = children.get('nextPageToken')
      
      if not page_token:
          break
import pdb
pdb.set_trace()

print_files_in_folder("0B_iCMJDnGmmtfjA2UHlUeENiMXlQWW53bmNLbkQ5MlNKYVRnM0NYQjNzbHVGN0RnUW1kX1k")