# Project_A. Automatically Update Files on Google Drive
## Functionality:

1. **Library Imports:**  
The script begins by importing necessary libraries, including those from the Google API for authentication and file operations.

2. **Path Definition:**
It defines two paths: path_JSON and path_file, representing the paths to the JSON key (for Google Drive API authentication) and the file to be uploaded, respectively.

3. **Google Drive API Setup:**
The script sets up the Google Drive API by using the provided JSON key (path_JSON) to obtain credentials for authentication.

4. **Folder Creation on Google Drive:**
A folder named 'Daily_Uploads' is created on Google Drive using the Drive API. The folder ID is retrieved for future reference.

5. **Sharing Folder with a Google Account:**
The script shares the created folder with a specified Google account using the account's email address. The specified account is given 'writer' permissions.

6. **Uploading Excel File to Google Drive:**
An Excel file is uploaded to the created folder on Google Drive. The file's name includes 'Daily_Upload_' followed by the current date. The uploaded file ID is printed if the upload is successful.

7. **Error Handling:**
The script includes exception handling to print any encountered errors during execution.

8. **Note:**
- Before running the script, you need to fill in the actual paths for path_JSON and path_file.
- Ensure that the specified Google account email (yourEmailOfGoogleAccount) is updated with the correct email address.
This script automates the process of creating a folder, sharing it with a designated Google account, and uploading a file to Google Drive.