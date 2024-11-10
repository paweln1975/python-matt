#!/usr/bin/env python3

# Reference:
# https://python3.info/fastapi/fastapi/http-files.html

#%% FastAPI Files
# MIME Type multipart/form-data
# File vs UploadFile -> use UploadFile
# Single File
# Multiple Files
# pip install python-multipart
# The files will be uploaded as "form data"



#%% MIME Type
# application/x-www-form-urlencoded - encoding for html forms without files
# multipart/form-data - encoding for html forms with files



#%% File
# File - receive content as bytes (stores in memory)



#%% UploadFile
# UploadFile - receives content as file (stores on disk)
# UploadFile.filename - original file name that was uploaded e.g. myimage.jpg
# UploadFile.content_type - MIME type e.g. image/jpeg
# UploadFile.file - file-like object which can be written to file
# UploadFile.write(data) - writes data (str or bytes) to the file
# UploadFile.read(size) - reads size (int) bytes/characters of the file
# UploadFile.seek(offset) - goes to the byte position offset (int) in the file
# UploadFile.close() - closes the file
# All methods are async and needs await