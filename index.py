import os
import datetime
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

path_JSON = r' ' #請填入JSON金鑰path
path_file = r' ' #請填入JSON金鑰path

try:
    # 設定Google Drive API金鑰憑證
    credentials = service_account.Credentials.from_service_account_file(
        path_JSON,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    # 設定Google Drive API
    drive_service = build('drive', 'v3', credentials=credentials)

    # 在Google Drive上創建目錄
    folder_metadata = {
        'name': 'Daily_Uploads',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
    folder_id = folder.get('id')

    # Create a permission. Here, your Google account is shared with the uploaded file.
    yourEmailOfGoogleAccount = '@gmail.com'  # <--- Please set your Email address of Google account.
    permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': yourEmailOfGoogleAccount,
    }
    drive_service.permissions().create(fileId=folder['id'], body=permission).execute()


    # 上傳Excel檔案到Google Drive
    file_metadata = {
        'name': f'Daily_Upload_{datetime.date.today()}.xlsx',
        'parents': [folder_id]
    }
    media = MediaFileUpload(path_file, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print(f'File ID: {file.get("id")}')

except Exception as e:
    print(f'Error: {e}')
